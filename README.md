# law-wiki-construction — Wiki pháp luật xây dựng

Wiki hệ thống hóa pháp luật xây dựng và quản lý dự án đầu tư xây dựng, có trích dẫn và kiểm chứng được. Phần đấu thầu đã có wiki riêng: https://github.com/phongsun01/law-wiki-bidding-v2.

**Trạng thái (Hoàn thành nghiệm thu Chặng 3, 2026-11-03):** Đã hoàn tất Ingest và nghiệm thu đạt 100% cả 3 chặng (Đợt 1: 15/15 câu; Đợt 2: 7/7 câu; Đợt 3: 6/6 câu - tổng cộng 28/28 câu kiểm thử Đạt, đối chiếu 100% với văn bản raw chính thức). Hệ thống wiki gồm 16 văn bản đã ingest toàn văn và 4 văn bản tham chiếu.

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
