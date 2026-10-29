# Bộ câu hỏi kiểm thử — wiki pháp luật xây dựng (skeleton v2.4, 2026-10-28)

Chặng 1a (Q01–Q06, Q06a, Q06b) đã được người dùng duyệt ngày 2026-10-28. Các câu của chặng 1b, 2, 3 vẫn là bản nháp, phải duyệt trước khi tới chặng đó.

Chỉ có câu hỏi, **chưa có đáp án**. Đáp án chỉ được xác định từ toàn văn trong `raw/` sau khi ingest. Các câu của chặng 1a đã duyệt xong ngày 2026-10-28, đủ điều kiện để ingest Luật 135 và NĐ 217 khi có toàn văn. Các câu chặng sau vẫn phải duyệt trước khi tới chặng đó.

Thay đổi so với skeleton v2.2:
- Q02: tách rõ 2 ý khi chấm — (a) tiêu chí phân loại, (b) hệ quả về thẩm quyền và trình tự thẩm định.
- Q04: bổ sung “theo từng nhóm dự án / nguồn vốn” và phân biệt cơ quan thẩm định với cơ quan phê duyệt dự án; văn bản dự kiến bổ sung Luật 135/2025 (dự kiến, chưa khóa cứng, sửa lại sau khi đọc toàn văn).
- Thêm Q06a (hình thức quản lý dự án) và Q06b (điều kiện khởi công). Dùng ký hiệu Q06a/Q06b để không phải đánh số lại Q07–Q20. Tổng bộ câu hỏi thành 22 câu.
- Các câu còn lại giữ nguyên wording của v2.2.

## Cách chấm (áp dụng cho mọi câu)

Một câu trả lời của wiki chỉ "Đạt" khi đủ cả 5 điều kiện:
1. Dẫn đúng Điều/Khoản/Điểm của đúng văn bản, truy được về file `raw/`.
2. Nêu đúng trạng thái hiệu lực, và điều khoản chuyển tiếp khi sự việc xảy ra trước 01/07/2026.
3. Không ghi tuyệt đối khi chưa có điều khoản (ví dụ không khẳng định NĐ 193 bãi bỏ NĐ 254 khi chưa tìm được điều khoản).
4. Nếu toàn văn chưa có nội dung đó: trả lời "chưa thấy trong nguồn", không suy diễn.
5. Phần đấu thầu: link sang wiki đấu thầu, không tự trả lời.

## Câu hỏi

| ID | Chặng | Câu hỏi | Văn bản dự kiến cần dẫn | Trích dẫn Điều/Khoản (điền sau ingest) | Kết quả | Ghi chú |
|---|---|---|---|---|---|---|
| Q01 | 1a | Hoạt động xây dựng có những chủ thể nào, và trách nhiệm chính của chủ đầu tư là gì? | Luật 135/2025 | Điều 3, Điều 9, Điều 35–41, Điều 59–63 | Đạt | Chủ thể gồm: người QĐĐT, CĐT, Ban QLDA, nhà thầu TV/TC/GS, CQCM về xây dựng. Trách nhiệm chính của CĐT quy định tại Điều 40, Điều 59, 60. |
| Q02 | 1a | Dự án đầu tư xây dựng được phân loại theo những tiêu chí nào? Việc phân loại đó ảnh hưởng gì đến (a) thẩm quyền thẩm định và (b) trình tự thẩm định? | Luật 135/2025, NĐ 217/2026 | Luật 135: Điều 17, 26, 27; NĐ 217: Điều 5, 31, 32, Phụ lục III, IV | Đạt | Tiêu chí phân loại: theo nguồn vốn/hình thức ĐT (đầu tư công, PPP, vốn khác), theo quy mô/tầm quan trọng (QTQG, A, B, C), theo công năng. Hệ quả thẩm quyền thẩm định BCNCKT phân định theo Điều 32 NĐ 217 (Bộ QL chuyên ngành, Ban QL KCN, UBND tỉnh/xã); trình tự thực hiện theo Điều 36 NĐ 217. |
| Q03 | 1a | Ai có thẩm quyền giao hoặc quyết định chủ đầu tư, theo điều kiện nào? | NĐ 217/2026, Luật 135/2025 | NĐ 217 Điều 6; Luật 135 Điều 9 | Chưa đạt | Cần đối chiếu chính xác câu chữ raw Điều 6 NĐ 217 và Điều 9 Luật 135 trước khi chấm lại. |
| Q04 | 1a | Theo từng nhóm dự án / nguồn vốn, cơ quan nào thẩm định báo cáo nghiên cứu khả thi, cơ quan phê duyệt dự án có khác cơ quan thẩm định không, và nội dung thẩm định gồm những gì? | Luật 135/2025, NĐ 217/2026 | Luật 135 Điều 26, 27, 28; NĐ 217 Điều 31, 32, 38, 39 | Chưa đạt | Đang rà soát lại thẩm quyền và nội dung thẩm định từng khoản để bảo đảm không suy diễn vượt phạm vi raw. |
| Q05 | 1a | Công trình nào phải có giấy phép xây dựng, trường hợp nào được miễn, hồ sơ gồm những gì? | Luật 135/2025, NĐ 217/2026 | Luật 135: Điều 43, 44; NĐ 217: Điều 49–62, Phụ lục II | Đạt | Công trình phải có GPXD trước khi khởi công trừ các trường hợp miễn tại Khoản 2 Điều 43 Luật 135 (bí mật NN, khẩn cấp, đầu tư công đặc biệt, công trình ĐTC do cấp thẩm quyền quyết định đầu tư, theo tuyến liên tỉnh/ngoài đô thị, nhà ở riêng lẻ nông thôn...). Hồ sơ quy định tại Điều 56–62 NĐ 217 (đơn, giấy tờ đất đai Điều 55, bản vẽ thiết kế, thông báo thẩm định). |
| Q06 | 1a | Dự án đã được phê duyệt trước 01/07/2026 nhưng chưa hoàn thành thì áp dụng quy định mới hay quy định cũ, và điều khoản chuyển tiếp nào quy định? | Luật 135/2025, NĐ 217/2026 | Luật 135: Điều 95 Khoản 1; NĐ 217: Điều 76 Khoản 1, 2, 3 | Đạt | Áp dụng chuyển tiếp: Dự án/thiết kế đã duyệt trước 01/07/2026 không phải duyệt lại; các hoạt động tiếp theo chưa thực hiện thì thực hiện theo Luật 135 (Điều 95 K1). Dự án/công trình đã có thông báo kết quả thẩm định trước ngày NĐ 217 có hiệu lực không phải thẩm định lại (NĐ 217 Điều 76 K1). |
| Q06a | 1a | Dự án đầu tư xây dựng có những hình thức quản lý dự án nào, chủ đầu tư được chọn hình thức nào trong trường hợp nào, và Ban quản lý dự án hoặc tư vấn quản lý dự án có trách nhiệm gì? | Luật 135/2025, NĐ 217/2026 | Luật 135 Điều 32; NĐ 217 Điều 44–48 | Chưa đạt | Cần đối chiếu kỹ quy định chủ đầu tư chọn hình thức tại Điều 44 Khoản 6 NĐ 217 và trách nhiệm trong raw. |
| Q06b | 1a | Điều kiện để được khởi công xây dựng là gì? | Luật 135/2025 | Luật 135 Điều 48 | Chưa đạt | Điều 48 raw có 3 khoản (khoản 1 có 5 điểm a–đ, khoản 2 và 3 quy định điều kiện riêng). Đang cập nhật đáp án khớp toàn văn. |
| Q07 | 1b | Hợp đồng xây dựng có những loại hợp đồng theo giá nào, và khi nào được điều chỉnh giá hợp đồng? | NĐ 210/2026 | | | |
| Q08 | 1b | Với hợp đồng trọn gói, trường hợp nào được điều chỉnh giá hoặc khối lượng? | NĐ 210/2026 | | | |
| Q09 | 1b | Điều kiện, mức và thời điểm tạm ứng hợp đồng xây dựng là gì? | NĐ 210/2026 | | | |
| Q10 | 1b | Khi thương thảo, hoàn thiện hợp đồng, nội dung nào được thương thảo và nội dung nào không? | NĐ 210/2026 (đối chiếu wiki đấu thầu) | | | |
| Q11 | 1b | Tổng mức đầu tư, dự toán xây dựng và giá gói thầu được xác định theo trình tự nào, và dùng định mức dự toán nào? | NĐ 206/2026, TT 36/2026, TT 37/2026 | | | |
| Q12 | 1b | Hợp đồng ký trước 01/07/2026 áp dụng NĐ 210/2026 hay quy định cũ? | NĐ 210/2026 | | | |
| Q13 | 2 | Nghiệm thu công trình xây dựng gồm những bước nào, ai chịu trách nhiệm? | NĐ 207/2026, TT 32/2026 | | | |
| Q14 | 2 | Thời hạn và trách nhiệm bảo hành công trình quy định thế nào, có khác nhau theo cấp công trình không? | NĐ 207/2026, TT 32/2026, TT 34/2026 | | | |
| Q15 | 2 | Công trình được phân cấp thế nào, và cấp công trình ảnh hưởng gì đến quản lý? | TT 34/2026 | | | |
| Q16 | 2 | Tổ chức, cá nhân cần điều kiện năng lực hoặc chứng chỉ nào để tham gia hoạt động xây dựng, và tra cứu ở CSDL quốc gia thế nào? | NĐ 212/2026, TT 39/2026 | | | |
| Q17 | 3 | Phân biệt quyết toán hợp đồng, thanh toán vốn đầu tư công và quyết toán vốn đầu tư dự án hoàn thành: văn bản nào điều chỉnh từng phần? | NĐ 210/2026, NĐ 254/2025, NĐ 193/2026 | | | |
| Q18 | 3 | Hồ sơ quyết toán vốn đầu tư dự án hoàn thành gồm những gì, và thời hạn lập, thẩm tra là bao lâu? | NĐ 193/2026, TT 63/2025 | | | |
| Q19 | 3 | **Câu kiểm tra tính thận trọng:** "NĐ 193/2026 đã bãi bỏ NĐ 254/2025 phải không?" | NĐ 193/2026, NĐ 254/2025 | | | Chỉ Đạt nếu wiki chỉ khẳng định khi dẫn được điều khoản bãi bỏ; nếu chưa có thì trả lời chưa kết luận. |
| Q20 | 3 | Bảo hiểm bắt buộc nào áp dụng trong hoạt động đầu tư xây dựng, và NĐ 220/2026 sửa đổi những điểm nào của NĐ 67/2023? | NĐ 220/2026, NĐ 67/2023 | | | |

## Quy tắc vận hành

- Cuối đợt 3: chạy toàn bộ 22 câu.
- Cuối mỗi chặng: chạy các câu của chặng đó và mọi câu của chặng trước nếu văn bản mới ingest có liên quan.
- Câu không Đạt: ghi vào cột Ghi chú và `wiki/LOG.md`, sửa trang, không sửa lặng lẽ; chạy lại.
- Bổ sung câu khi gặp tình huống thật chưa có trong bộ này.
