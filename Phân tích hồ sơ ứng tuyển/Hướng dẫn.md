# Hướng dẫn: Tự động hoá nghiệp vụ Nhân sự với AI (Antigravity Agent)

Chào mừng các bạn học viên đến với khóa huấn luyện thực hành ứng dụng Trí tuệ Nhân tạo hệ Agentic và quá trình tự động hoá cho doanh nghiệp! Dưới đây là bức tranh toàn cảnh giải mã cách bạn hợp tác với tổ hợp AI **Antigravity** để biến ý tưởng dở dang thành một hệ thống quản trị tuyển dụng thực thụ mà không cần viết lệnh code nào.

## 1. Tư duy cốt lõi: Làm việc theo vòng lặp "Sprint-centric"
Điều tối kị khi áp dụng AI vĩ mô là đưa 1 "chỉ thị khổng lồ" chứa 20 gạch đầu dòng khác nhau bắt hệ thống làm cùng lúc. Thay vào đó, bí quyết là chẻ nhỏ thành các chặng (Sprint):
- Giao cho AI tạo và giữ một tệp "La bàn" là `todo.md`.
- Lên kế hoạch đánh dấu từng nấc (VD: Sprint 1 thiết lập folder, Sprint 2 tạo file giả lập, Sprint 3 viết Code).
- Yêu cầu AI "chạy hoàn thành Sprint 1, tích dấu `[x]` rồi báo cáo trước khi sang Sprint 2". Như vậy Antigravity sẽ được tối ưu sự tĩnh lặng, không bao giờ mất trí nhớ cấu trúc (Context windows).

## 2. Giải mã thuật toán xương sống: Mô hình luồng IPO (Input - Process - Output)

Thay vì làm việc theo cảm tính như các chatbot thông thường, tổ hợp Antigravity tư duy theo chuỗi "Chốt trạm" khép kín. Tại mỗi chốt chạm, hệ thống tuân thủ tuyệt đối cơ chế: **Nhận nguyên liệu (Input) -> Chạy tiến trình xử lý tự động (Process) -> Trả ra thành phẩm (Output)**. Hãy nhìn vào Case Study ứng tuyển phía trên để hiểu logic này:

### Bước 1: Khởi tạo và Tiền xử lý dữ liệu (Pre-processing)
- **[I] - INPUT (Nguyên liệu thô):** Lệnh yêu cầu cấp thiết từ người dùng để dọn dẹp mớ rác lưu trữ (hoặc các CV hỗn độn).
- **[P] - PROCESS:** AI tự động thiết lập các folder rành mạch (`01_Ho_so_dau_vao`, `02_Thu_tuyen_dung`...), tạo sẵn file `README.md` lưu bối cảnh và **tự đặt luật định danh** ép mọi hồ sơ sau này phải lưu chuẩn theo cấu trúc `[CV_ID]_[JD_ID]`. 
- **[O] - OUTPUT (Sản phẩm):** Một bộ khung Không gian làm việc cực kỳ ngăn nắp, dữ liệu quy chuẩn để chuẩn bị cho LLM nhúng tay vào.

### Bước 2: Trí tuệ AI Khai thác & Mockup (AI Extraction & Mocking)
- **[I] - INPUT:** Bản tiêu chuẩn vị trí (JD). Và 1 Prompt "Làm giả lập 10 hồ sơ mô phỏng" (hoặc truyền CV gốc vào).
- **[P] - PROCESS:** LLM (Trí tuệ nhân tạo lõi) kích hoạt. Nó thay con người tự tưởng tượng, nhận diện các thực thể học thuật (Tên tuổi, Học vấn, Kinh nghiệm), đâm chéo từ khóa để tự bóc tách và "chấm điểm".
- **[O] - OUTPUT:** Vô số những dữ liệu/bản nháp phân tích chi tiết siêu thực được trút vào kho đệm `03_Phan_tich_trung_gian` dưới định dạng mà máy tính đọc được (Markdown, JSON).

### Bước 3: Chuyển hoá và Định tuyến (Data Transform)
- **[I] - INPUT:** Khối chữ nghĩa lộn xộn/dữ liệu thô vừa bóc tách ở Bước 2.
- **[P] - PROCESS:** Hành động "Transform" bẻ gãy ngôn ngữ tự nhiên để gói vào Bảng biểu. Thêm thuật toán định tuyến tự động phân làn: Hồ sơ có mã JD là `[MKT]` thì quét lùa hết đưa về bảng MKT. Máy móc tự thực thi không cần con người ngó ngàng.
- **[O] - OUTPUT:** 5 Bảng báo cáo lưu tách lẻ theo từng phòng ban (`.csv`). Đồng thời sinh ra 1 siêu Bảng tính quy tụ dữ liệu toàn doanh nghiệp `Tong_hop_tat_ca_vi_tri.csv` lưu về `04_Du_lieu_tong_hop`.

### Bước 4: Đóng gói Phần mềm & Nghiệm thu Dữ liệu (Validation GUI)
- **[I] - INPUT:** Trọn bộ thư mục các file CSV tẻ nhạt. Và sự khao khát ra quyết định nhanh gọn từ Lãnh đạo.
- **[P] - PROCESS:** Agent trực tiếp đóng vai "Kỹ sư PM" viết file Python (`hr_csv_manager.py`). Tích hợp thư viện Tkinter dựng khung giao diện. Cài cắm hàm **Audit (Kiểm duyệt)** để tự lôi số dòng của bảng các phòng ban cộng lại đem trừ đi số dòng siêu bảng tính Master nhằm truy tìm sai lệch rò rỉ hồ sơ.
- **[O] - OUTPUT:** Chuyên viên HR chỉ việc đưa chuột bấm mở một cái App Desktop trên Window cực lấp lánh (GUI), đảm bảo "Toàn vẹn Dữ liệu 100%". Rút ngắn thứ mà trước đây tốn 2 tháng outsource xuống còn 15 phút.

## 3. Tổng kết thông điệp
Bạn chính là **"Kiến trúc sư của những tác nhân"** (AI Orchestrator). 
- Thay vì xắn tay vào làm việc tay chân, định hướng của bạn là dùng kĩ năng **Phân tích yêu cầu (Prompt)** + **Tổ chức workflow**.
- Khi tư duy làm việc của bạn kết nối với tốc độ thực thi của Agentic AI, bạn có thể build ra trọn vẹn phần mềm điều phối nhân sự mà xưa kia tốn của bạn vài trăm triệu và 3 tháng outsource.

-- *Bài thực hành kết thúc.* --
