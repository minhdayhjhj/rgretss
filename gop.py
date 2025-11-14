import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
from faker import Faker
import random
import requests
import datetime

# Kiểm tra kết nối mạng
def check_connection():
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except:
        return False

# Lấy vị trí và thời tiết
def get_location_weather():
    try:
        ip_data = requests.get("https://ipinfo.io").json()
        city = ip_data.get("city", "Unknown")
        country = ip_data.get("country", "Unknown")
        loc = ip_data.get("loc", "0,0")
        lat, lon = loc.split(",")
        weather = requests.get(f"https://wttr.in/{lat},{lon}?format=%t").text.strip()
        return f"{city}, {country} - {weather}"
    except:
        return "Không thể lấy thời tiết"

# Tạo email
def generate_emails():
    domain = domain_entry.get().strip()
    try:
        count = int(count_entry.get())
    except:
        messagebox.showerror("Lỗi", "Số lượng email không hợp lệ!")
        return

    filename = file_entry.get().strip()
    country = country_var.get()
    add_number = number_var.get()
    char = char_entry.get().strip()

    if not domain or not filename or not country:
        messagebox.showerror("Thiếu thông tin", "Vui lòng điền đầy đủ thông tin.")
        return

    locale_map = {
        'US': 'en_US', 'India': 'hi_IN', 'VN': 'vi_VN',
        'Canada': 'en_CA', 'Singapore': 'en_SG', 'Sez': 'fr_FR'
    }

    fake = Faker(locale_map.get(country, 'en_US'))

    # Tên Việt Nam đặc biệt
    if country == 'VN':
        names = "Nguyen,Tran,Le,Pham,Ho,Huynh,Hoang,Phan,Vu,Vo,Dang,Bui,Do,Hua,Ly,Cao,Dinh,Doan,Dao,Duc,Duong,Giang,Ha,Han,Khuat,Khuong,La,Lam,Luc,Mai,Mac,Nghe,Nghiem,Ngo,Nguyen,Pho,Quach,Quang,Quan,Quy,Ta,Thai,Thach,Than,Thang,Thao,Thi,Thich,Thinh,Thoi,Tieu,To,Trang,Trinh,Truong,Tu,Ung,Vien,Vuong,Vuu,Yen,Van"
        name_list = names.split(',')
    else:
        name_list = [fake.first_name().lower() for _ in range(count)]

    emails = []
    for _ in range(count):
        name = random.choice(name_list).lower()
        if add_number:
            name += str(random.randint(10, 99))
        if char.lower() != 'không' and char != '':
            name += char
        email = f"{name}@{domain}"
        emails.append(email)

    try:
        with open(filename, 'w') as f:
            for email in emails:
                f.write(email + '\n')
        result_box.delete(1.0, tk.END)
        result_box.insert(tk.END, "\n".join(emails))
        messagebox.showinfo("Thành công", f"Đã tạo {count} email và lưu vào {filename}")
    except Exception as e:
        messagebox.showerror("Lỗi ghi file", str(e))

# Giao diện chính
app = ThemedTk(theme="arc")
app.title("Gen Mail V2 Pro")
app.geometry("700x600")
app.configure(bg="#1e1e2f")

# Header
header = tk.Label(app, text="✉️ Gen Mail V2 Pro", font=("Helvetica", 20, "bold"), bg="#1e1e2f", fg="cyan")
header.pack(pady=10)

# Thời tiết
weather_label = tk.Label(app, text=get_location_weather(), font=("Arial", 10), bg="#1e1e2f", fg="lightgreen")
weather_label.pack()

# Form
form_frame = ttk.Frame(app)
form_frame.pack(pady=20)

ttk.Label(form_frame, text="Tên miền email:").grid(row=0, column=0, sticky="w")
domain_entry = ttk.Entry(form_frame, width=30)
domain_entry.grid(row=0, column=1)

ttk.Label(form_frame, text="Số lượng email:").grid(row=1, column=0, sticky="w")
count_entry = ttk.Entry(form_frame, width=30)
count_entry.grid(row=1, column=1)

ttk.Label(form_frame, text="Tên file lưu:").grid(row=2, column=0, sticky="w")
file_entry = ttk.Entry(form_frame, width=30)
file_entry.grid(row=2, column=1)

ttk.Label(form_frame, text="Quốc gia:").grid(row=3, column=0, sticky="w")
country_var = tk.StringVar()
country_menu = ttk.Combobox(form_frame, textvariable=country_var, values=["US", "India", "VN", "Canada", "Singapore", "Sez"])
country_menu.grid(row=3, column=1)

ttk.Label(form_frame, text="Thêm ký tự vào tên:").grid(row=4, column=0, sticky="w")
char_entry = ttk.Entry(form_frame, width=30)
char_entry.grid(row=4, column=1)

number_var = tk.BooleanVar()
ttk.Checkbutton(form_frame, text="Thêm số vào tên", variable=number_var).grid(row=5, column=1, sticky="w")

# Nút tạo
ttk.Button(app, text="Tạo Email", command=generate_emails).pack(pady=10)

# Kết quả
result_box = tk.Text(app, height=12, bg="#2e2e3f", fg="white", font=("Courier", 10))
result_box.pack(fill=tk.BOTH, padx=20, pady=10, expand=True)

# Kiểm tra mạng
if not check_connection():
    messagebox.showwarning("Không có mạng", "Vui lòng kiểm tra kết nối Internet!")

app.mainloop()
