## 2026-10-28 — Ingest Chặng 1a (Luật 135/2025/QH15 & Nghị định 217/2026/NĐ-CP)

- Ingest toàn văn Luật Xây dựng số 135/2025/QH15 từ `raw/luat-135-2025.md` (8 Chương, 95 Điều, sha256: `22828f486b96a3399b8e17f93fa9287e2d4eb92968f272dd411680efa06325ff`). Cập nhật status thành `ingested`, ghi nhận hiệu lực 01/07/2026 (ngoại lệ một số điều hiệu lực sớm từ 01/01/2026: K2, K3 Điều 43, Điều 71, K3, K4, K5 Điều 95) và bãi bỏ Luật Xây dựng 50/2014/QH13.
- Ingest toàn văn Nghị định số 217/2026/NĐ-CP từ `raw/nd-217-2026.md` (5 Chương, 76 Điều, 4 Phụ lục, sha256: `7b2f3c2ca6d10cbce1c0d22119944e567e03ba7adcc0b979eb5f55372a68e229`). Cập nhật status thành `ingested`, ghi nhận hiệu lực 01/07/2026 và bãi bỏ Nghị định số 175/2024/NĐ-CP.
- Chấm đạt 8/8 câu hỏi kiểm thử Chặng 1a (Q01, Q02, Q03, Q04, Q05, Q06, Q06a, Q06b) trong `tests/cau-hoi-kiem-thu.md`, điền đầy đủ trích dẫn Điều/Khoản và căn cứ pháp lý chính xác.
- Cập nhật `wiki/INDEX.md`: chuyển trạng thái Luật 135/2025 và NĐ 217/2026 thành `ingested`.
- Kiểm tra qua `scripts/lint.py`: 0 errors, 0 warnings.

# LOG — Wiki pháp luật xây dựng

## 2026-10-28 — Skeleton v2.4 (chưa ingest)

- Áp dụng ngày hiệu lực do người dùng cung cấp, đã xác nhận ngày 2026-10-28, CHƯA đối chiếu toàn văn: TT 32/2026 hiệu lực 2026-07-01; NĐ 104/2026 hiệu lực 2026-03-31. Cập nhật ở frontmatter, thân trang và INDEX của 2 trang tương ứng. Các ngày này phải đối chiếu lại với toàn văn khi ingest (TT 32 ở đợt 2, NĐ 104 là tham chiếu).
- Chặng 1a đã duyệt: Q01–Q06, Q06a, Q06b (8 câu) được người dùng duyệt ngày 2026-10-28. Cập nhật tiêu đề và ghi chú duyệt trong `tests/cau-hoi-kiem-thu.md`. Các câu chặng 1b, 2, 3 vẫn là bản nháp.
- Sửa lỗi nhỏ về ngày tháng: tiêu đề plan đổi thành v1.6 ngày 2026-10-28; README và INDEX của skeleton đổi thành v2.4 ngày 2026-10-28; SCHEMA mục 6 đổi nhãn thành "theo plan v1.6".
- Giữ nguyên, do người dùng tự làm: toàn văn đợt 1a và cách trích Điều (làm thủ công có đối chiếu, hoặc script mới đã kiểm tra mẫu). Chưa push, chưa ingest.


## 2026-10-28 — Sửa 3 điểm nhỏ trong skeleton v2.3 (chưa ingest, chưa đổi version)

- `wiki/SCHEMA.md` mục 6: đổi "theo plan v1.2" thành "theo plan v1.5" (nội dung đợt vốn đã đúng theo v1.5, chỉ sai nhãn).
- `scripts/lint.py`: thêm kiểm tra `group` (chỉ I, III, IV), `tag` (chỉ taxonomy ở SCHEMA mục 5) và định dạng ngày tháng (`YYYY-MM-DD` hoặc `"unknown"`) cho `issued_date`, `effective_date`, `last_verified`. Bản skeleton hiện tại vẫn qua lint 0 lỗi sau khi thêm các kiểm tra này.
- Chốt trang chủ đề xuyên văn bản thuộc `wiki/syntheses/` (không phải `wiki/concepts/`): 3 trang đợt 1 (`chuyen-tiep-01-07-2026`, `hop-dong-xay-dung-dieu-chinh-gia-thanh-toan`, `chi-phi-dinh-muc-du-toan`) và 1 trang đợt 3 (`thanh-toan-quyet-toan-3-tang`); liệt kê giữ chỗ ở `wiki/INDEX.md` (chưa dùng wikilink vì file chưa tồn tại), ghi quy tắc ở `wiki/SCHEMA.md` mục 2b; `scripts/lint.py` miễn kiểm tra orphan cho `wiki/concepts/` và `wiki/syntheses/`.
- Lưu ý giữ nguyên: NĐ 193/2026 và NĐ 254/2025 vẫn ở `pending-ingest` trong skeleton; chỉ chuyển sang `warning` sau khi đã ingest đợt 3 mà chưa tìm được điều khoản bãi bỏ (lint bắt buộc trang `warning` phải có file `raw/` và mục "Cảnh báo").

## 2026-10-27 — Skeleton v2.3 (chưa ingest)

- `tests/cau-hoi-kiem-thu.md`: thay bằng bản cập nhật chặng 1a (22 câu): sửa Q02 và Q04, thêm Q06a (hình thức quản lý dự án) và Q06b (điều kiện khởi công). Vẫn là câu hỏi nháp, chưa có đáp án.
- Cách trích Điều: `extract_vb_phapluat.py` không tìm thấy nên không dựa vào. Đợt 1a làm thủ công có đối chiếu, hoặc dùng một script tách Điều mới đã kiểm tra mẫu trước.
- `scripts/lint.py`: thêm kiểm tra cấu trúc bảng câu hỏi (7 cột, mã câu hỏi không trùng, chặng hợp lệ).

## 2026-10-27 — Skeleton v2.2 (chưa ingest)

- Thêm trường `source_url` vào frontmatter của mọi trang `documents/` (null cho tới khi ingest); lint cảnh báo nếu trang đã ingest mà chưa có.
- `raw/README.md`: quy tắc OCR — giữ file gốc, bản sửa OCR là file riêng và ghi LOG, không sửa file gốc rồi giữ `sha256` cũ.
- `tests/cau-hoi-kiem-thu.md`: thêm cột "Trích dẫn Điều/Khoản" để trống cho tới khi ingest.
- Ghi chú: `extract_vb_phapluat.py` (viết cho văn bản đấu thầu) chỉ là ứng viên trích Điều, chưa thử trên văn bản xây dựng; không ghi là "pipeline dùng lại" cho tới khi thử xong.

## 2026-10-27 — Skeleton v2.1 (chưa ingest)

- Quyết định của người dùng: giữ TT 32, TT 36, TT 37; bỏ NĐ 347/2025; nhóm V là danh sách hoãn (chưa quyết định).
- Bỏ stub NĐ 347/2025 và mọi liên kết tới nó. Còn 4 stub tham chiếu: NĐ 67/2023, TT 96/2021, Luật NSNN 89/2025, NĐ 104/2026.
- Hiệu lực TT 36 và TT 37: 2026-07-01 (người dùng cung cấp, chưa đối chiếu toàn văn). TT 32 vẫn "unknown".
- Stub tham chiếu đổi `batch: 3` thành `batch: "ref"` để không bị hiểu là ingest đợt 3; lint kiểm tra quy tắc này.
- INDEX: nhóm V thành "Danh sách hoãn".
- Thêm `tests/cau-hoi-kiem-thu.md` (câu hỏi soạn trước, chưa có đáp án).

## 2026-10-27 — Skeleton v2 (chưa ingest)

Sửa skeleton theo 6 mục rà soát:
- Đổi đợt cho khớp plan v1.2: NĐ 217 sang đợt 1a; NĐ 207 sang đợt 2. Đợt 1 tách chặng 1a, 1b.
- Thêm 8 stub: TT 32, TT 36, TT 37 (core); NĐ 67/2023, TT 96/2021 (văn bản gốc được sửa đổi); Luật NSNN 89/2025, NĐ 347/2025, NĐ 104/2026 (nhóm IV, tham chiếu). NĐ 347/2025 đã bị bỏ ở v2.1.
- Bỏ mọi nhắc tới NĐ 274/2026 (dự án đầu tư kinh doanh, ngoài phạm vi).
- Frontmatter thêm `subject`, `role`, `stage`, `tags`, `source_file`, `sha256`, `last_verified`; SCHEMA mô tả 5 giá trị `status`.
- Thêm `raw/`, `wiki/concepts/`, `wiki/syntheses/`, `scripts/lint.py`.
- Viết lại README và INDEX theo trạng thái repo.
- Ghi chú: ngày hiệu lực của TT 32, TT 36, TT 37 và các stub tham chiếu chưa có trong bảng nguồn nên để "unknown".

## 2026-10-26 — Skeleton v1 để review (chưa phải version, chưa ingest)

- Tạo 12 stub `documents/` (nhóm I + nhóm III), kèm SCHEMA, INDEX, LOG.
- Nguồn duy nhất: bảng hệ thống hóa 24 văn bản do người dùng cung cấp ngày 2026-10-26.
- Cảnh báo đã ghi: nhóm đấu thầu trong bảng nguồn cũ hơn wiki đấu thầu; mâu thuẫn NĐ 193 / NĐ 254 chưa có điều khoản bãi bỏ chính xác; lỗi chính tả "Thượng thảo" đã sửa thành "Thương thảo".
