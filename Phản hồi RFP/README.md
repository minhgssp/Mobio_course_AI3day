# Hệ thống Quản trị & Tự động hoá Phản hồi RFP

**Tầm nhìn:** Đây là "Cỗ máy làm thầu tự động" dành cho team PD/AM/PO/SA.
> Hệ thống áp dụng quy trình đếm ngược, thay vì người làm cày lại từ đầu, tác nhân AI sẽ quét qua thư viện quá khứ, nhặt những câu trả lời xuất sắc nhất, đối chiếu với thầu mới, tính toán chi phí tuỳ chỉnh và xuất thẳng ra hồ sơ nháp chỉ trong vài phút.

## Vận hành I-P-O nội khu:
- `01_RFP_Dau_Vao/` : [INPUT] Chứa file thầu nguyên bản và các email mời thầu.
- `02_Kho_Tai_Lieu_Lich_Su/` : [BASE] "Não bộ". Kho tri thức lịch sử dưới dạng Database để AI tra cứu.
- `03_Checklist_Va_Format/` : [PROCESS] Chứa các mẫu khung sườn làm việc và Form phản hồi. 
- `04_Draft_Va_Cham_Diem/` : [OUTPUT] Chứa hồ sơ 1st draft, 2nd Draft và bảng bot chạy chấm điểm rà soát.
- `05_Bao_Gia_MD/` : [OUTPUT] Bản giá Manday cho đội ngũ Sale.

*Mọi tác vụ thực thi được theo dõi tại `todo_rfp.md`.*
