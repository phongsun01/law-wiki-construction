# LLM Wiki Schema — Pháp luật xây dựng và quản lý dự án đầu tư xây dựng (skeleton v2.4)

> Skeleton v2.3, 2026-10-27. Chưa ingest toàn văn. Mọi văn bản core còn `pending-ingest`.

## 1. Phạm vi (Domain)

Wiki này hệ thống hóa **pháp luật xây dựng và quản lý dự án đầu tư xây dựng** (quản lý hoạt động xây dựng, chất lượng, chi phí, hợp đồng, quyết toán). **Không** bao gồm: thực tiễn thi công/kỹ thuật, TCVN/QCVN toàn văn, và **không** viết lại phần đấu thầu (đã có wiki riêng).

## 2. Cấu trúc

```
law-wiki-construction/
├── wiki/
│   ├── documents/    # 15 văn bản core + 4 stub tham chiếu
│   ├── concepts/     # khái niệm pháp lý đơn lẻ (làm sau khi ingest)
│   ├── syntheses/    # trang chủ đề xuyên văn bản (làm theo từng đợt, xem dưới)
│   ├── SCHEMA.md     # file này
│   ├── INDEX.md      # mục lục + đợt ingest + trạng thái
│   └── LOG.md        # nhật ký thay đổi
├── raw/              # toàn văn chính thức, bất biến (xem raw/README.md)
├── tests/            # bộ câu hỏi kiểm thử, soạn trước khi ingest
└── scripts/lint.py   # kiểm tra chất lượng, chạy sau mỗi chặng ingest
```

## 2b. Trang chủ đề xuyên văn bản (syntheses/) — chốt ngày 2026-10-28

- `syntheses/` chứa các trang chủ đề xuyên văn bản, tổng hợp từ nhiều văn bản, phải trích dẫn Điều/Khoản của văn bản gốc, không tạo ra fact pháp lý mới. `concepts/` chứa khái niệm pháp lý đơn lẻ, không phải trang chủ đề xuyên văn bản.
- Các trang chủ đề đã chốt trong plan, **chưa tạo trong skeleton** (chỉ liệt kê ở INDEX để không mất dấu, chưa dùng wikilink vì file chưa tồn tại):
  - Đợt 1: `syntheses/chuyen-tiep-01-07-2026.md`, `syntheses/hop-dong-xay-dung-dieu-chinh-gia-thanh-toan.md`, `syntheses/chi-phi-dinh-muc-du-toan.md`
  - Đợt 3: `syntheses/thanh-toan-quyet-toan-3-tang.md`
- Khi tạo trang chủ đề, đổi dòng liệt kê tương ứng trong INDEX thành wikilink tới file thật. Trang trong `concepts/` và `syntheses/` là điểm vào theo chủ đề nên `scripts/lint.py` miễn kiểm tra orphan cho hai thư mục này.

## 3. Quy tắc bắt buộc (học từ wiki đấu thầu v2.3.0)

- **Stub trước, full-text sau.** Chỉ rời `pending-ingest` khi đã có file `raw/` toàn văn chính thức. Bảng tóm tắt không phải nguồn.
- **Link, không copy, phần đấu thầu.** Chuẩn là wiki đấu thầu https://github.com/phongsun01/law-wiki-bidding-v2 (v2.3.0): Luật 22/2023/QH15 (đã sửa đổi), NĐ 214/2025, NĐ 349/2026, TT 79/2025, TT 134/2026 (thay TT 80/2025). Không dùng bảng nguồn ngày 2026-10-26 để cập nhật nhóm đấu thầu: bảng đó cũ hơn wiki đấu thầu (thiếu NĐ 349 và TT 134, liệt kê TT 80 như còn hiệu lực, nhầm ngày ban hành 04/08/2025 với ngày hiệu lực của NĐ 214 và TT 79 trong khi ngày hiệu lực theo wiki đấu thầu là 01/10/2025).
- **Văn bản bị thay thế giữ làm lưu vết**, đặt `status: superseded`, không xóa.
- **Tham chiếu only.** Nhóm IV (ngân sách) chỉ ở mức stub tham chiếu. Ingest toàn văn các lĩnh vực ngoài xây dựng sẽ biến wiki này thành wiki ngân sách + đất đai + môi trường; nếu muốn mở rộng thì làm kế hoạch riêng.
- **Nhóm V là danh sách hoãn** (NĐ 85/2025, Luật Đất đai 31/2024, Luật Bảo vệ môi trường 72/2020, Luật Tổ chức chính quyền địa phương 72/2025): chưa quyết định, không có stub, giữ tên trong INDEX để không mất dấu.
- **Văn bản sửa đổi phải có văn bản gốc.** Ví dụ NĐ 220/2026 sửa NĐ 67/2023, TT 63/2025 sửa TT 96/2021: đọc và ghi chéo hai chiều, có stub cho văn bản gốc.
- **Không ghi tuyệt đối khi chưa có điều khoản.** Ví dụ: chưa được ghi "NĐ 193 bãi bỏ NĐ 254" hay "toàn bộ hệ thống đồng bộ từ 01/07/2026" cho tới khi có điều khoản chuyển tiếp và phạm vi bãi bỏ chính xác. Dự án bắt đầu trước 01/07/2026 có thể có điều khoản chuyển tiếp riêng.
- **Không sửa lặng lẽ.** Văn bản mới, sửa đổi, hết hiệu lực: ghi LOG, cập nhật INDEX, kiểm tra lại các trang liên quan, đổi `last_verified`.
- **Tên file:** lowercase, gạch nối: `luat-135-2025.md`, `nd-207-2026.md`, `tt-39-2026.md`.
- **Thông tư đọc kèm nghị định** mà nó hướng dẫn; ghi liên kết hai chiều.

## 4. Frontmatter của trang `documents/`

```yaml
---
document_id: nd-210-2026          # trùng tên file
title: "Nghị định số 210/2026/NĐ-CP"
subject: "Hợp đồng xây dựng"
issued_date: 2026-06-15           # hoặc "unknown" nếu bảng nguồn chưa có
effective_date: 2026-07-01        # hoặc "unknown"
status: pending-ingest            # xem 4.1
role: core                        # core | reference
group: "III"                      # I, III (core); III, IV (reference)
batch: 1                          # core: 1 | 2 | 3 ; reference: "ref"
stage: "1b"                       # core: 1a | 1b | 2 | 3 ; reference: "ref"
tags: [hop-dong-xay-dung]         # lấy từ taxonomy mục 5
source_note: "..."
source_file: null                 # đường dẫn raw/..., ví dụ raw/nd-210-2026.pdf
source_url: null                  # URL nguồn chính thức (Công báo, cổng chính thức); trang đã ingest nên có
sha256: null                      # sha256 của file raw
last_verified: null               # ngày đối chiếu toàn văn gần nhất
---
```

### 4.1 Giá trị `status`

| status | Ý nghĩa | Điều kiện lint |
|---|---|---|
| `pending-ingest` | Mới là stub, chưa có toàn văn | `source_file`, `sha256`, `last_verified` để `null` |
| `ingested` | Đã có toàn văn và đã viết trang đầy đủ | Bắt buộc có file `raw/`, `sha256` khớp, `last_verified`; nên có `source_url` (lint cảnh báo nếu trống) |
| `warning` | Đã ingest nhưng còn điểm chưa kiểm chứng được (ví dụ cặp NĐ 193 / NĐ 254) | Như `ingested`, và trang phải có mục "Cảnh báo" |
| `superseded` | Đã bị thay thế, giữ làm lưu vết | Như `ingested` |
| `reference` | Stub tham chiếu, không ingest sâu | Chỉ dùng với `role: reference`, và bắt buộc `batch: "ref"`, `stage: "ref"` |

`batch: "ref"` nghĩa là văn bản không thuộc đợt ingest nào. Nó chỉ được ingest sâu khi cần đọc kèm một văn bản core, và khi đó phải ghi LOG.

## 5. Taxonomy tag

`quan-ly-hoat-dong-xay-dung`, `chat-luong-cong-trinh`, `nang-luc-csdl`, `cap-cong-trinh`, `chi-phi-dau-tu-xay-dung`, `dinh-muc-du-toan`, `hop-dong-xay-dung`, `quyet-toan-von`, `thanh-toan-von`, `bao-hiem-xay-dung`, `ngan-sach`.

## 6. Đợt ingest (theo plan v1.6)

- **Đợt 1a:** Luật 135/2025, NĐ 217/2026.
- **Đợt 1b:** NĐ 210/2026, NĐ 206/2026, TT 36/2026, TT 37/2026.
- **Đợt 2:** NĐ 207/2026, TT 32/2026, NĐ 212/2026, TT 39/2026, TT 34/2026.
- **Đợt 3:** NĐ 193/2026, NĐ 254/2025, TT 63/2025, NĐ 220/2026.
- **Tham chiếu (`batch: "ref"`, không ingest theo đợt):** NĐ 67/2023, TT 96/2021, Luật NSNN 89/2025, NĐ 104/2026.

## 7. Cổng chất lượng mỗi chặng

1. `python3 scripts/lint.py` không có lỗi.
2. Chạy bộ câu hỏi kiểm thử liên quan trong `tests/cau-hoi-kiem-thu.md` (bộ câu hỏi của chặng phải được soạn xong trước khi ingest chặng đó): mỗi câu trả lời phải dẫn đúng Điều/Khoản, đúng văn bản, đúng trạng thái hiệu lực.
3. Cập nhật INDEX và LOG, rồi mới trình duyệt chặng kế tiếp.
