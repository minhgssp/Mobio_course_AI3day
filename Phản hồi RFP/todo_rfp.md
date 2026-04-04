# LUỒNG ĐIỀU PHỐI DỰ ÁN: TỰ ĐỘNG HOÁ PHẢN HỒI THẦU (RFP)

---

## 🎯 Góc nhìn Kinh doanh (Business Value)
Dự án được xây dựng nhằm giải phóng quy trình làm thầu rườm rà cho đội PD, PO, SA và AM. Giảm thiểu 50-80% thời gian xử lý thủ công (Copy-paste hồ sơ cũ, đếm số liệu, gõ lại form). Đảm bảo tính nhất quán của văn phong trả lời thầu và loại bỏ hoàn toàn các rủi ro chết người (Sót yêu cầu bắt buộc, Lệch báo giá) nhờ cơ chế Rà soát & Tự động tính toán Manday.

---

## 📅 Sprint-centric: Đường ray thực thi

### Sprint 1: Thiết lập Kiến trúc Không gian số & Luật lệ (Rule Base)
- [ ] R-S1-T1: Khởi tạo cấu trúc 5 phân hệ Folder cốt lõi chạy dọc theo luồng I-P-O.
- [ ] R-S1-T2: Số hóa "Ma trận tuyên bố đáp ứng" và "Checklist hồ sơ" thành các file mẫu (Template) chốt chặt dưới dạng Markdown/CSV.
- [ ] R-S1-T3: Tạo file bối cảnh chung `README.md` cấp phát quyền cho thư mục.

### Sprint 2: Giả lập Database khổng lồ (Mockup & Training Data)
- [ ] R-S2-T1: Tạo Kho lưu trữ tài liệu thầu quá khứ. Giả lập 20 bộ "Câu Hỏi - Trả Lời" thầu của Mobio (Lưu định dạng siêu dẫn JSON/CSV).
- [ ] R-S2-T2: Giả lập 1 kịch bản Thông báo thầu RFP mới từ khách (Word/PDF) chứa gài cắm các yếu tố gây rủi ro (Bắt cung cấp Source Code).

### Sprint 3: Tự động Bóc tách và Đối khớp Dữ liệu (AI Matching & Routing)
- [ ] R-S3-T1: Đọc tệp RFP mới, tự động tách "Yếu tố rủi ro" (Risk) lên đầu báo cáo.
- [ ] R-S3-T2: Trích xuất các tiêu chí thầu -> So khớp 100% với Kho Lịch Sử. Tự động gắn tag: Đã có, Cần Customize hoặc Không Align.
- [ ] R-S3-T3: Bắn dữ liệu thô ra bảng `1st Draft` cho người dùng Review.

### Sprint 4: Kiểm Duyệt, Định Dạng & Báo Giá (Validation & Quotation)
- [ ] R-S4-T1: Kích hoạt Agent đóng vai Giám Khảo, dọc chéo hồ sơ 1st Draft để đấm điểm 1-10 và đánh giá độ hợp lý.
- [ ] R-S4-T2: Tự động format `2nd draft` chuẩn chỉnh (In đậm nội dung chốt chặn, font chữ đồng bộ).
- [ ] R-S4-T3: Chạy Engine báo giá. Lọc tính năng "Cần Customize", tính toán Manday * Rate ra chi phí báo giá (Quote).

### Sprint 5: Đóng gói App UI Quản trị Thầu (RFP Commander)
- [ ] R-S5-T1: Lập trình hệ thống App giao diện Desktop (Python GUI).
- [ ] R-S5-T2: Tích hợp nút Kiểm định hồ sơ và Quản lý Kho lịch sử ngay lồng trong phần mềm.
- [ ] R-S5-T3: Sinh báo cáo `walkthrough.md` và bàn giao toàn hệ thống cho Lãnh đạo PD.
