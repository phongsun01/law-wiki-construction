# raw/ — toàn văn chính thức (bất biến)

- Mỗi văn bản một file, đặt tên theo `document_id`: `raw/luat-135-2025.pdf`, `raw/nd-217-2026.docx`...
- Ưu tiên bản có lớp chữ (Word hoặc PDF có text). Bản scan phải kiểm tra lỗi OCR trước khi ingest.
- Giữ file gốc đúng như đã nhận; không sửa nội dung file sau khi đưa vào. Nếu có bản mới, hoặc bản đã sửa lỗi OCR, thêm thành file riêng (ví dụ `raw/<document_id>-ocr-fix.<đuôi>`) và ghi LOG. Không sửa file gốc rồi giữ nguyên `sha256` cũ.
- Sau khi thêm file, cập nhật frontmatter của trang tương ứng:
  - `source_file: raw/<tên file>`
  - `source_url: <URL nguồn chính thức>` (để `null` nếu nhận file offline, và ghi nguồn vào LOG)
  - `sha256: <kết quả của lệnh sha256sum raw/<tên file>>`
  - `last_verified: <ngày đối chiếu>`
- Văn bản pháp luật chính thức dùng được. TCVN/QCVN có bản quyền thì không đưa toàn văn vào repo.
