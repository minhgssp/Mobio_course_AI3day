import os
import csv
import tkinter as tk
from tkinter import ttk, messagebox

class HRCSVManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Phần mềm Quản lý và Đối chiếu CSV Tuyển Dụng")
        self.geometry("950x550")
        
        # Thư mục chứa dữ liệu
        self.data_dir = os.path.join(os.path.dirname(__file__), "04_Du_lieu_tong_hop")
        
        # === Bố cục giao diện ===
        self.frame_left = tk.Frame(self, width=250, bg="#e0e0e0")
        self.frame_left.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        
        self.frame_right = tk.Frame(self)
        self.frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # -- Bên trái: Danh sách File + Nút --
        tk.Label(self.frame_left, text="Thư mục: 04_Du_lieu_tong_hop", font=("Arial", 10, "bold"), bg="#e0e0e0").pack(pady=(5, 10))
        
        self.file_listbox = tk.Listbox(self.frame_left, font=("Arial", 11), selectbackground="#4a90e2")
        self.file_listbox.pack(fill=tk.BOTH, expand=True)
        self.file_listbox.bind('<<ListboxSelect>>', self.on_file_select)
        
        self.btn_compare = tk.Button(self.frame_left, text="Kiểm tra Đối chiếu Dữ liệu", 
                                     bg="#28a745", fg="white", font=("Arial", 11, "bold"), 
                                     command=self.compare_files, pady=8)
        self.btn_compare.pack(fill=tk.X, pady=15)
        
        # -- Bên phải: Bảng dữ liệu Grid --
        tk.Label(self.frame_right, text="Khu vực khảo sát Data CSV", font=("Arial", 12, "bold"), fg="#333").pack(pady=(0, 10))
        
        # Setup Treeview for grid
        self.tree_frame = tk.Frame(self.frame_right)
        self.tree_frame.pack(fill=tk.BOTH, expand=True)
        
        self.tree = ttk.Treeview(self.tree_frame, show="headings")
        
        y_scrollbar = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        x_scrollbar = ttk.Scrollbar(self.frame_right, orient=tk.HORIZONTAL, command=self.tree.xview)
        x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.tree.configure(yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Tải danh sách file vào giao diện
        self.load_file_list()

    def load_file_list(self):
        """Đọc thư mục và add vào listbox"""
        if not os.path.exists(self.data_dir):
            messagebox.showerror("Lỗi thư mục", f"Không tìm thấy thư mục lưu CSV tại:\n{self.data_dir}")
            return
            
        files = [f for f in os.listdir(self.data_dir) if f.endswith('.csv')]
        for f in files:
            self.file_listbox.insert(tk.END, f)
            
    def on_file_select(self, event):
        """Sự kiện khi click vào một file trong danh sách"""
        selection = self.file_listbox.curselection()
        if not selection:
            return
            
        filename = self.file_listbox.get(selection[0])
        filepath = os.path.join(self.data_dir, filename)
        
        self.display_csv(filepath)
        
    def display_csv(self, filepath):
        """Đọc và in dữ liệu ra Grid"""
        # Xóa grid cũ
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                headers = next(reader, [])
                
                self.tree["columns"] = headers
                for col in headers:
                    self.tree.heading(col, text=col)
                    self.tree.column(col, width=150, anchor=tk.W)
                    
                for row in reader:
                    self.tree.insert("", tk.END, values=row)
        except Exception as e:
            messagebox.showerror("Lỗi nạp dữ liệu", f"Không thể đọc file {os.path.basename(filepath)}\nChi tiết: {str(e)}")

    def compare_files(self):
        """Hàm thuật toán đọc Master CSV và đối chiếu tổng CSV con"""
        master_file = os.path.join(self.data_dir, "Tong_hop_tat_ca_vi_tri.csv")
        
        if not os.path.exists(master_file):
            messagebox.showerror("Lỗi đối chiếu", "File Master 'Tong_hop_tat_ca_vi_tri.csv' không tồn tại!")
            return
            
        try:
            # Đọc tổng bản ghi của master
            master_count = sum(1 for _ in open(master_file, 'r', encoding='utf-8')) - 1
            
            child_count = 0
            child_files = [f for f in os.listdir(self.data_dir) if f.endswith('.csv') and f != "Tong_hop_tat_ca_vi_tri.csv"]
            
            for file in child_files:
                filepath = os.path.join(self.data_dir, file)
                count = sum(1 for _ in open(filepath, 'r', encoding='utf-8')) - 1
                child_count += count
                
            if master_count == child_count and master_count > 0:
                msg = (f"CÁC FILE DỮ LIỆU ĐÃ KHỚP NHAU HOÀN TOÀN!\n\n"
                       f"Tổng số hồ sơ tại File Master: {master_count}\n"
                       f"Tổng số hồ sơ nhặt từ file vị trí lẻ: {child_count}")
                messagebox.showinfo("Báo cáo đối chiếu thành công", msg)
            elif master_count == 0:
                messagebox.showwarning("Cảnh báo", "Hệ thống không tìm thấy bất kỳ dữ liệu nào (bản ghi = 0).")
            else:
                msg = (f"CẢNH BÁO: PHÁT HIỆN LỆCH DỮ LIỆU!\n\n"
                       f"Master: chứa {master_count} hồ sơ.\n"
                       f"Các file phân nhánh gộp lại: chứa {child_count} hồ sơ.\n\n"
                       "Vui lòng xem xét chạy lại module trích xuất.")
                messagebox.showwarning("Cảnh báo sai lệch", msg)
                
        except Exception as e:
            messagebox.showerror("Lỗi thuật toán", f"Phát sinh lỗi chạy đối chiếu: {str(e)}")


if __name__ == "__main__":
    app = HRCSVManager()
    app.mainloop()
