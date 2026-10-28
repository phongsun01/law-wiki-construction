"""Linter cho law-wiki-construction.

Chạy: python3 scripts/lint.py   (cần PyYAML)
Phần kiểm tra wikilink học từ law-wiki-bidding-v2/scripts/lint.py.
Sửa ngày 2026-10-28: thêm kiểm tra group, tag (theo SCHEMA mục 5) và
định dạng ngày tháng; miễn orphan cho wiki/concepts/ và wiki/syntheses/
(vì trang chủ đề là điểm vào, được liệt kê ở INDEX, không nhất thiết
phải có văn bản khác link tới).
"""
import datetime
import hashlib
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
WIKI = REPO / "wiki"
DOCS = WIKI / "documents"

REQUIRED = ["document_id", "title", "subject", "issued_date", "effective_date", "status", "role",
            "group", "batch", "stage", "tags", "source_note", "source_file", "source_url", "sha256", "last_verified"]
STATUSES = {"pending-ingest", "ingested", "warning", "superseded", "reference"}
ROLES = {"core", "reference"}
FULL = {"ingested", "warning", "superseded"}
# Nhóm và tag lấy đúng từ wiki/SCHEMA.md (mục 5 và frontmatter mẫu).
# Nhóm II là đấu thầu (wiki riêng, link ngoài) và nhóm V là danh sách hoãn,
# nên không có trang documents/ nào được ghi group II hay V.
GROUPS = {"I", "III", "IV"}
TAGS = {"quan-ly-hoat-dong-xay-dung", "chat-luong-cong-trinh", "nang-luc-csdl",
        "cap-cong-trinh", "chi-phi-dau-tu-xay-dung", "dinh-muc-du-toan",
        "hop-dong-xay-dung", "quyet-toan-von", "thanh-toan-von",
        "bao-hiem-xay-dung", "ngan-sach"}


def valid_date(value):
    """Ngày hợp lệ là 'unknown', hoặc ngày thật dạng YYYY-MM-DD.

    PyYAML tự đổi 2026-07-01 thành đối tượng date, nên chấp nhận cả hai dạng.
    """
    if value is None:
        return False
    if isinstance(value, (datetime.date, datetime.datetime)):
        return True
    if isinstance(value, str):
        if value == "unknown":
            return True
        try:
            datetime.datetime.strptime(value, "%Y-%m-%d")
            return True
        except ValueError:
            return False
    return False
WIKILINK = re.compile(r"\[\[([^\]\|#]+)(?:#([^\]\|]+))?(?:\|([^\]]+))?\]\]")


def parse_fm(path):
    txt = path.read_text(encoding="utf-8")
    if not txt.startswith("---"):
        return None, "Missing frontmatter"
    parts = txt.split("---", 2)
    if len(parts) < 3:
        return None, "Malformed frontmatter"
    try:
        return (yaml.safe_load(parts[1]) or {}), None
    except Exception as e:  # noqa: BLE001
        return None, f"Invalid YAML: {e}"


def main():
    errors, warnings = [], []
    files = list(WIKI.rglob("*.md"))
    by_rel = {f.relative_to(WIKI).as_posix()[:-3]: f for f in files}
    by_stem = {}
    for f in files:
        by_stem.setdefault(f.stem, []).append(f)
    incoming = {f: 0 for f in files}

    # 1. wikilinks
    total = 0
    for f in files:
        rel = f.relative_to(WIKI).as_posix()
        for m in WIKILINK.finditer(f.read_text(encoding="utf-8")):
            total += 1
            target = m.group(1).strip().replace("\\", "/")
            target = target[:-3] if target.endswith(".md") else target
            tf = by_rel.get(target) or (by_stem.get(Path(target).name) or [None])[0]
            if tf is None:
                errors.append(f"[{rel}] Broken link: [[{m.group(1)}]]")
            else:
                incoming[tf] += 1
    print(f"Files: {len(files)}   Wikilinks: {total}")

    # 2. frontmatter của documents/
    index_txt = (WIKI / "INDEX.md").read_text(encoding="utf-8")
    counts = {}
    for f in sorted(DOCS.glob("*.md")):
        rel = f.relative_to(WIKI).as_posix()
        fm, err = parse_fm(f)
        if err:
            errors.append(f"[{rel}] {err}")
            continue
        for k in REQUIRED:
            if k not in fm:
                errors.append(f"[{rel}] Missing key: {k}")
        if fm.get("document_id") != f.stem:
            errors.append(f"[{rel}] document_id '{fm.get('document_id')}' != tên file")
        st, role = fm.get("status"), fm.get("role")
        if st not in STATUSES:
            errors.append(f"[{rel}] status '{st}' không hợp lệ")
        if role not in ROLES:
            errors.append(f"[{rel}] role '{role}' không hợp lệ")
        if role == "reference" and st != "reference":
            errors.append(f"[{rel}] role reference phải có status reference")
        if role == "core" and st == "reference":
            errors.append(f"[{rel}] role core không được có status reference")
        if role == "core":
            if fm.get("stage") not in {"1a", "1b", "2", "3"}:
                errors.append(f"[{rel}] core phải có stage 1a/1b/2/3")
            if fm.get("batch") not in {1, 2, 3}:
                errors.append(f"[{rel}] core phải có batch 1/2/3")
        if role == "reference" and (fm.get("batch") != "ref" or fm.get("stage") != "ref"):
            errors.append(f"[{rel}] reference phải có batch \"ref\" và stage \"ref\" (không thuộc đợt ingest nào)")
        if not fm.get("tags"):
            errors.append(f"[{rel}] Missing tags")
        else:
            tags = fm["tags"] if isinstance(fm["tags"], list) else [fm["tags"]]
            for t in tags:
                if t not in TAGS:
                    errors.append(f"[{rel}] tag '{t}' ngoài taxonomy SCHEMA mục 5")
        if fm.get("group") not in GROUPS:
            errors.append(f"[{rel}] group '{fm.get('group')}' không hợp lệ (chỉ I, III, IV; II là đấu thầu wiki riêng, V là danh sách hoãn)")
        for key in ("issued_date", "effective_date"):
            if key in fm and not valid_date(fm.get(key)):
                errors.append(f"[{rel}] {key} '{fm.get(key)}' không đúng dạng YYYY-MM-DD hoặc 'unknown'")
        if fm.get("last_verified") is not None and not valid_date(fm.get("last_verified")):
            errors.append(f"[{rel}] last_verified '{fm.get('last_verified')}' không đúng dạng YYYY-MM-DD")
        counts[st] = counts.get(st, 0) + 1

        sf, sha, lv = fm.get("source_file"), fm.get("sha256"), fm.get("last_verified")
        if st in FULL:
            if not sf or not sha or not lv:
                errors.append(f"[{rel}] status {st} cần source_file, sha256, last_verified")
            else:
                rf = REPO / str(sf)
                if not rf.is_file():
                    errors.append(f"[{rel}] source_file không tồn tại: {sf}")
                elif hashlib.sha256(rf.read_bytes()).hexdigest() != str(sha).lower():
                    errors.append(f"[{rel}] sha256 không khớp file {sf}")
            if not fm.get("source_url"):
                warnings.append(f"[{rel}] đã ingest nhưng chưa có source_url (ghi nguồn chính thức nếu có)")
            if st == "warning" and "## Cảnh báo" not in f.read_text(encoding="utf-8"):
                errors.append(f"[{rel}] status warning cần mục '## Cảnh báo'")
            if fm.get("effective_date") == "unknown":
                warnings.append(f"[{rel}] đã ingest nhưng effective_date vẫn unknown")
        elif st in {"pending-ingest", "reference"}:
            if sf or sha or lv or fm.get("source_url"):
                warnings.append(f"[{rel}] status {st} nhưng đã có source_file/source_url/sha256/last_verified: đổi status?")
            if list((REPO / "raw").glob(f"{f.stem}.*")):
                warnings.append(f"[{rel}] đã có file raw/{f.stem}.* nhưng status vẫn {st}")

        # INDEX phải có dòng cho văn bản, và status khớp
        line = next((l for l in index_txt.splitlines() if f"documents/{f.stem}" in l), None)
        if line is None:
            errors.append(f"[{rel}] không có trong INDEX.md")
        elif st not in line:
            warnings.append(f"[{rel}] INDEX ghi trạng thái khác với frontmatter ({st})")

    # 2b. bộ câu hỏi kiểm thử
    tf = REPO / "tests" / "cau-hoi-kiem-thu.md"
    if not tf.is_file():
        errors.append("Thiếu tests/cau-hoi-kiem-thu.md")
    else:
        seen = set()
        n_q = 0
        for line in tf.read_text(encoding="utf-8").splitlines():
            if not re.match(r"\|\s*Q\d+[a-z]?\s*\|", line):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            n_q += 1
            qid = cells[0]
            if len(cells) != 7:
                errors.append(f"[tests] {qid}: bảng phải có 7 cột, đang có {len(cells)}")
                continue
            if qid in seen:
                errors.append(f"[tests] mã câu hỏi trùng: {qid}")
            seen.add(qid)
            if cells[1] not in {"1a", "1b", "2", "3"}:
                errors.append(f"[tests] {qid}: chặng '{cells[1]}' không hợp lệ")
            if not cells[2] or not cells[3]:
                errors.append(f"[tests] {qid}: thiếu câu hỏi hoặc văn bản dự kiến")
        print(f"Câu hỏi kiểm thử: {n_q}")

    # 3. orphan
    # Trang concepts/ và syntheses/ là điểm vào theo chủ đề, được liệt kê
    # ở INDEX, nên miễn orphan cho hai thư mục này.
    exempt = {"INDEX.md", "LOG.md", "SCHEMA.md"}
    for f, n in incoming.items():
        rel = f.relative_to(WIKI).as_posix()
        if n == 0 and rel not in exempt and not rel.startswith(("concepts/", "syntheses/")):
            errors.append(f"Orphan (không có wikilink trỏ tới): {rel}")

    print("Status:", ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    print(f"Errors: {len(errors)}   Warnings: {len(warnings)}")
    for w in warnings:
        print("  WARN ", w)
    for e in errors:
        print("  ERROR", e)
    if errors:
        print("LINT FAILED")
        return 1
    print("LINT OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
