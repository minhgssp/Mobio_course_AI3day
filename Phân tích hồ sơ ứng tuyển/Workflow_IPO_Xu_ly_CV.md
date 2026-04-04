# System Workflow: Quy trình Xử lý CV Tự động hoá (Step-by-Step IPO Model)

Với mô hình này, luồng đi của dữ liệu từ khi Doanh nghiệp bắt đầu tuyển dụng tới khi nghiệm thu được bẻ tách thành các "Chốt trạm" (Steps). Tại mỗi chốt chạm, quy trình luôn phải thỏa mãn nguyên lý đầu vào biến đổi thành đầu ra **(Input -> Process -> Output)** độc lập.

## Bước 1: Thu thập và Tiền xử lý Dữ liệu (Pre-processing)
Giai đoạn biến những rác thải đa nguồn, mất cấu trúc thành mớ tài nguyên có cấu trúc đồng nhất.

- **[I] - INPUT (Nguyên liệu thô):**
  - Mớ hỗn độn hồ sơ (Raw CV) chưa chuẩn hóa với đủ định dạng: PDF, Docx, Hình ảnh scan,... đổ về từ Email, LinkedIn, Web Form.
  - Các mã Yêu cầu Tuyển dụng (JD-ID) được đặt ra từ Trưởng phòng chuyên môn.
- **[P] - PROCESS (Thực thi tự động):**
  - Agent tự động quét và tải toàn bộ File về khu vực tập kết.
  - Đọc nội dung file và gán nhãn Đổi Tên theo quy ước Định danh ghép: `[CV_ID]_[JD_ID]`.
  - Cắt vỡ các lớp mã hóa của PDF/Word để ép toàn bộ chúng về định dạng văn bản đọc được (Thuần Text/Markdown).
- **[O] - OUTPUT (Thành phẩm thu được):**
  - Một thư mục `01_Ho_so_dau_vao` cực kỳ ngăn nắp, chứa các tập hồ sơ đã được "Dán nhãn định danh" và sẵn sàng cho AI đọc.

---

## Bước 2: AI Khai thác & Chấm điểm (AI Extraction & Matching)
Giai đoạn mà "máy móc đóng vai con người" để đọc hiểu văn bản, chứ không chỉ tìm từ khóa cứng nhắc.

- **[I] - INPUT:**
  - Các hồ sơ đã sạch, đã sẵn sàng text từ Bước 1.
  - File thông tin Tiêu chuẩn Công việc gốc (Job Description) tương ứng ở `02_Thu_tuyen_dung`.
- **[P] - PROCESS:**
  - Chạy Engine cấp phát Prompt kèm hồ sơ đưa cho LLM thẩm định.
  - LLM tiến hành *Nhận diện Thực thể (Entity Recognition)* để gắp lấy Tên, SĐT, Email tránh nhầm lẫn.
  - Thực hiện *So khớp Ngữ nghĩa (Semantic Matching)* để đâm chéo từ khóa kinh nghiệm làm việc của CV vào tiêu chuẩn JD, ra điểm đánh giá mức độ phù hợp (vd: 85%).
- **[O] - OUTPUT:**
  - Các tệp dữ liệu trung gian chứa nội dung phân tích chi tiết, sạch sẽ, chuẩn bóc tách (thường lưu dưới dạng JSON hoặc Markdown), thả vào `03_Phan_tich_trung_gian`.

---

## Bước 3: Chuẩn hoá Hệ thống & Phân tuyến (Data Transform & Routing)
Giai đoạn biến những gì AI "nghĩ" dưới dạng văn bản học thuật thành những bảng tính mà Sếp và Kế toán hiểu được.

- **[I] - INPUT:**
  - Kho tàng phân tích trung gian (những dòng text/chấm điểm) rời rạc của Bước 2.
- **[P] - PROCESS:**
  - Render cấu trúc: Ráp nối các chuỗi đánh giá thành một cấu trúc Bảng Biểu (Cột & Hàng dọc).
  - Data Routing (Định tuyến): Thuật toán đếm và lọc. Hồ sơ có dán nhãn thuộc về Marketing `[MKT]` thì quét lùa hết vào chung 1 bảng. Hồ sơ khối kỹ thuật thì gộp vào bảng IT.
  - Gộp thành chuỗi Data Master đính kèm tất thảy phòng ban để lên Báo cáo mỏ neo điểm.
- **[O] - OUTPUT:**
  - 5 Bảng báo cáo `Tên_Phòng_Ban.csv` phân dạt riêng rẽ. 
  - 1 "Siêu Bảng tính" `Tong_hop_tat_ca_vi_tri.csv` tổng quát, tập kết toàn bộ tại lõi `04_Du_lieu_tong_hop`.

---

## Bước 4: Kiểm duyệt Trực quan & Hành động (Validation & Action)
Chặn chốt chặn an toàn cuối cùng, bảo vệ kết quả dữ liệu trước khi "Hạ chốt".

- **[I] - INPUT:**
  - Toàn bộ các bảng tính CSV ném ra từ Bước 3.
- **[P] - PROCESS:**
  - Kích hoạt phần mềm GUI nội bộ (`hr_csv_manager.py`).
  - Giao diện trực quan tải hết dữ liệu lên màn hình thay cho Excel.
  - Chạy thuật toán "Kiểm định bù trừ" (Audit Sum): Phần mềm tự cộng gộp số lượng Record lẻ ở từng phòng ban và đo tương hỗ với số Record dòng đếm từ siêu bảng tính Master. Phản ứng cảnh báo Xanh / Vàng chớp nhoáng.
- **[O] - OUTPUT:**
  - Tín hiệu xác minh "Toàn vẹn Dữ liệu" 100%. 
  - Có thể kích hoạt hệ thống Action Trigger (Tự động nảy số gửi Email/Zalo chốt đậu hoặc từ chối ứng viên ngay lập tức).
