# law-wiki-construction — Wiki pháp luật xây dựng

Wiki hệ thống hóa pháp luật xây dựng và quản lý dự án đầu tư xây dựng, có trích dẫn và kiểm chứng được. Phần đấu thầu đã có wiki riêng: https://github.com/phongsun01/law-wiki-bidding-v2.

**Trạng thái (Chặng 1b hoàn thành nghiệm thu, 2026-10-30):** Đã hoàn tất Ingest Đợt 1 gồm cả Chặng 1a (Luật 135/2025, NĐ 217/2026) và Chặng 1b (NĐ 210/2026, NĐ 206/2026, TT 36/2026, TT 37/2026). Đạt toàn bộ 15/15 câu hỏi kiểm thử đã duyệt (8 câu Chặng 1a: Q01–Q06, Q06a, Q06b và 7 câu Chặng 1b: Q07–Q12) với trích dẫn chuẩn xác từng Điều, Khoản, Điểm khớp 100% toàn văn raw.

## Cấu trúc

- `wiki/SCHEMA.md` — quy chuẩn, frontmatter, giá trị `status`, taxonomy
- `wiki/INDEX.md` — mục lục, đợt ingest, trạng thái
- `wiki/LOG.md` — nhật ký thay đổi
- `wiki/documents/` — mỗi văn bản một trang
- `raw/` — toàn văn chính thức (xem `raw/README.md`)
- `tests/cau-hoi-kiem-thu.md` — bộ câu hỏi kiểm thử, soạn trước khi ingest
- `scripts/lint.py` — kiểm tra chất lượng

## Quy trình ingest một văn bản

0. Trước khi ingest chặng nào: bộ câu hỏi của chặng đó trong `tests/` phải được soạn và duyệt xong.
1. Đưa toàn văn chính thức vào `raw/<document_id>.<đuôi>`.
2. Đối chiếu ngày ban hành, hiệu lực, điều khoản chuyển tiếp, văn bản sửa đổi/bãi bỏ.
3. Viết trang đầy đủ thay stub; điền `source_file`, `source_url`, `sha256`, `last_verified`; đổi `status`.
4. Cập nhật INDEX và LOG.
5. Chạy `python3 scripts/lint.py` (cần `pip install pyyaml`) và bộ câu hỏi kiểm thử.

## Đợt ingest

| Đợt | Văn bản |
|---|---|
| 1a | Luật 135/2025, NĐ 217/2026 |
| 1b | NĐ 210/2026, NĐ 206/2026, TT 36/2026, TT 37/2026 |
| 2 | NĐ 207/2026, TT 32/2026, NĐ 212/2026, TT 39/2026, TT 34/2026 |
| 3 | NĐ 193/2026, NĐ 254/2025, TT 63/2025, NĐ 220/2026 |

Chỉ sang đợt sau khi đợt trước qua lint và bộ câu hỏi kiểm thử.
