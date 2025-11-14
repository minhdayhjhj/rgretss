import sys
import subprocess
import tempfile
import requests
import customtkinter as ctk
from tkinter import messagebox
import json
import os
from datetime import datetime, timedelta

URL = "https://raw.githubusercontent.com/minhdayhjhj/ttctiktok/refs/heads/main/ttctiktok.py"
TDS_URL = "https://raw.githubusercontent.com/minhdayhjhj/ch-n-qu-ae-i-tao-b-ngu/refs/heads/main/doimktds.py"
GOLIKE_URL = "https://raw.githubusercontent.com/minhdayhjhj/greklghfdkljgdjsdkfgjsl/refs/heads/main/AutoTheads.py"
GOLIKE_IG_URL = "https://raw.githubusercontent.com/minhdayhjhj/t-ibij-i-n/refs/heads/main/golikeig.py"
GOLIKE_IG_V1_URL = "https://raw.githubusercontent.com/minhdayhjhj/thtrehrhtrhrhr/refs/heads/main/golikeigv1.py"
GOLIKE_IG_V2_URL = "https://raw.githubusercontent.com/minhdayhjhj/nguthichiu/refs/heads/main/golikeigv2.py"
DVMXH_URL = "https://raw.githubusercontent.com/minhdayhjhj/KhangDevxcod/refs/heads/main/DVMXH.py"
GOLIKE_TIKTOK_URL = "https://raw.githubusercontent.com/minhdayhjhj/r-threkgrekal/refs/heads/main/goliketiktok.py"
GOLIKE_TWITTER_URL = "https://raw.githubusercontent.com/minhdayhjhj/5yhrthtdrhd/refs/heads/main/Goliketwitter.py"
GOLIKE_YOUTUBE_URL = "https://raw.githubusercontent.com/minhdayhjhj/ru-tytt/refs/heads/main/golikeYTB.py"  # New YouTube URL added
GOLIKE_LINKEDIN_URL = "https://raw.githubusercontent.com/minhdayhjhj/ghthstr/refs/heads/main/Linkedin.py"  # New LinkedIn URL added

# Bỏ toàn bộ cơ chế key và đăng nhập, vào thẳng menu chính

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self, user_key=None):
        super().__init__()
        self.user_key = user_key
        self.title("TOOL GỘP BY KHANGDEVX")
        self.geometry("1000x800")  # Further increased height for better spacing
        self.minsize(900, 750)     # Adjusted minimum size
        self.resizable(True, True)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Gradient-style background with modern colors
        self.main_frame = ctk.CTkFrame(
            self,
            corner_radius=25,
            fg_color=("#ffffff", "#0a0e27"),
            border_width=2,
            border_color=("#e0e0e0", "#1e2749"),
        )
        self.main_frame.grid(row=0, column=0, padx=25, pady=25, sticky="nsew")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Scrollable frame for buttons
        self.scrollable_frame = ctk.CTkScrollableFrame(
            self.main_frame, corner_radius=15, fg_color="transparent"
        )
        self.scrollable_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        # Modern fonts with better sizing
        title_font = ctk.CTkFont(family="Segoe UI", size=42, weight="bold")
        subtitle_font = ctk.CTkFont(family="Segoe UI", size=18, weight="normal")
        button_font = ctk.CTkFont(family="Segoe UI", size=16, weight="bold")
        section_font = ctk.CTkFont(family="Segoe UI", size=20, weight="bold")

        # Header section with gradient effect
        header_frame = ctk.CTkFrame(self.scrollable_frame, fg_color="transparent")
        header_frame.grid(row=0, column=0, pady=(30, 15), padx=50, sticky="ew")

        ctk.CTkLabel(
            header_frame,
            text="⚡ TOOL GỘP",
            font=title_font,
            text_color=("#0066ff", "#00d4ff"),
        ).pack()
        ctk.CTkLabel(
            header_frame,
            text="BY KHANGDEVX",
            font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"),
            text_color=("#ff6b35", "#ffa94d"),
        ).pack(pady=(5, 0))

        # Subtitle with modern styling
        ctk.CTkLabel(
            self.scrollable_frame,
            text="🚀 Bộ công cụ tổng hợp tiện ích mạnh mẽ",
            font=subtitle_font,
            text_color=("#666666", "#b8b8b8"),
        ).grid(row=1, column=0, pady=(0, 20), padx=50)

        # ===== SOCIAL MEDIA SECTION =====
        social_section = ctk.CTkFrame(self.scrollable_frame, fg_color="transparent")
        social_section.grid(row=2, column=0, padx=60, pady=(15, 10), sticky="ew")
        
        ctk.CTkLabel(
            social_section,
            text="📱 CÔNG CỤ MẠNG XÃ HỘI",
            font=section_font,
            text_color=("#4da6ff", "#66ccff"),
        ).pack(pady=(0, 15))

        # Button container with better spacing
        button_frame = ctk.CTkFrame(social_section, fg_color="transparent")
        button_frame.pack(fill="x", padx=15, pady=5)
        button_frame.grid_columnconfigure(0, weight=1)

        # Modern TikTok button with shadow effect
        self.action_btn = ctk.CTkButton(
            button_frame,
            text="🎯 TƯƠNG TÁC CHÉO TIKTOK",
            height=65,
            corner_radius=15,
            font=button_font,
            fg_color=("#0066ff", "#0052cc"),
            hover_color=("#0052cc", "#003d99"),
            border_width=2,
            border_color=("#0052cc", "#00d4ff"),
            text_color=("#ffffff", "#ffffff"),
            command=lambda: self.start_fetch(URL),
        )
        self.action_btn.grid(row=0, column=0, padx=15, pady=10, sticky="ew")

        # Golike TikTok button with TikTok brand colors
        self.golike_tiktok_btn = ctk.CTkButton(
            button_frame,
            text="🎵 GOLIKE TIKTOK",
            height=65,
            corner_radius=15,
            font=button_font,
            fg_color=("#69C9D0", "#3A86FF"),
            hover_color=("#3A86FF", "#265C9E"),
            border_width=2,
            border_color=("#3A86FF", "#72DDF7"),
            text_color=("#ffffff", "#ffffff"),
            command=lambda: self.start_fetch(GOLIKE_TIKTOK_URL),
        )
        self.golike_tiktok_btn.grid(row=1, column=0, padx=15, pady=10, sticky="ew")

        # Golike YouTube button with YouTube brand colors
        self.golike_youtube_btn = ctk.CTkButton(
            button_frame,
            text="▶️ GOLIKE YOUTUBE",
            height=65,
            corner_radius=15,
            font=button_font,
            fg_color=("#ff0000", "#cc0000"),  # YouTube red gradient
            hover_color=("#cc0000", "#990000"),
            border_width=2,
            border_color=("#cc0000", "#ff3333"),
            text_color=("#ffffff", "#ffffff"),
            command=lambda: self.start_fetch(GOLIKE_YOUTUBE_URL),
        )
        self.golike_youtube_btn.grid(row=2, column=0, padx=15, pady=10, sticky="ew")

        # Golike Twitter button with Twitter brand colors
        self.golike_twitter_btn = ctk.CTkButton(
            button_frame,
            text="🐦 GOLIKE TWITTER",
            height=65,
            corner_radius=15,
            font=button_font,
            fg_color=("#1da1f2", "#0a56b3"),
            hover_color=("#0a56b3", "#073a7e"),
            border_width=2,
            border_color=("#0a56b3", "#52b6f5"),
            text_color=("#ffffff", "#ffffff"),
            command=lambda: self.start_fetch(GOLIKE_TWITTER_URL),
        )
        self.golike_twitter_btn.grid(row=3, column=0, padx=15, pady=10, sticky="ew")

        # Golike LinkedIn button with LinkedIn brand colors
        self.golike_linkedin_btn = ctk.CTkButton(
            button_frame,
            text="💼 GOLIKE LINKEDIN",
            height=65,
            corner_radius=15,
            font=button_font,
            fg_color=("#0077b5", "#005582"),  # LinkedIn blue gradient
            hover_color=("#005582", "#003d66"),
            border_width=2,
            border_color=("#005582", "#0099e5"),
            text_color=("#ffffff", "#ffffff"),
            command=lambda: self.start_fetch(GOLIKE_LINKEDIN_URL),
        )
        self.golike_linkedin_btn.grid(row=4, column=0, padx=15, pady=10, sticky="ew")

        # Modern Golike Instagram button with pink gradient
        self.golike_ig_btn = ctk.CTkButton(
            button_frame,
            text="📸 GOLIKE INSTAGRAM",
            height=65,
            corner_radius=15,
            font=button_font,
            fg_color=("#ec4899", "#db2777"),
            hover_color=("#db2777", "#be185d"),
            border_width=2,
            border_color=("#db2777", "#f472b6"),
            text_color=("#ffffff", "#ffffff"),
            command=lambda: self.start_fetch(GOLIKE_IG_URL),
        )
        self.golike_ig_btn.grid(row=5, column=0, padx=15, pady=10, sticky="ew")

        # Modern Golike Instagram V1 button with orange gradient
        self.golike_ig_v1_btn = ctk.CTkButton(
            button_frame,
            text="📱 GOLIKE INSTAGRAM V1",
            height=65,
            corner_radius=15,
            font=button_font,
            fg_color=("#f97316", "#ea580c"),
            hover_color=("#ea580c", "#c2410c"),
            border_width=2,
            border_color=("#ea580c", "#fb923c"),
            text_color=("#ffffff", "#ffffff"),
            command=lambda: self.start_fetch(GOLIKE_IG_V1_URL),
        )
        self.golike_ig_v1_btn.grid(row=6, column=0, padx=15, pady=10, sticky="ew")

        # New Golike Instagram V2 button with cyan gradient
        self.golike_ig_v2_btn = ctk.CTkButton(
            button_frame,
            text="🆕 GOLIKE INSTAGRAM V2",
            height=65,
            corner_radius=15,
            font=button_font,
            fg_color=("#06b6d4", "#0891b2"),
            hover_color=("#0891b2", "#0e7490"),
            border_width=2,
            border_color=("#0891b2", "#22d3ee"),
            text_color=("#ffffff", "#ffffff"),
            command=lambda: self.start_fetch(GOLIKE_IG_V2_URL),
        )
        self.golike_ig_v2_btn.grid(row=7, column=0, padx=15, pady=10, sticky="ew")

        # Modern Golike button with green gradient (Threads)
        self.golike_btn = ctk.CTkButton(
            button_frame,
            text="💬 GOLIKE AUTO THREADS",
            height=65,
            corner_radius=15,
            font=button_font,
            fg_color=("#10b981", "#059669"),
            hover_color=("#059669", "#047857"),
            border_width=2,
            border_color=("#059669", "#34d399"),
            text_color=("#ffffff", "#ffffff"),
            command=lambda: self.start_fetch(GOLIKE_URL),
        )
        self.golike_btn.grid(row=8, column=0, padx=15, pady=10, sticky="ew")

        # ===== UTILITIES SECTION =====
        util_section = ctk.CTkFrame(self.scrollable_frame, fg_color="transparent")
        util_section.grid(row=3, column=0, padx=60, pady=(25, 10), sticky="ew")
        
        ctk.CTkLabel(
            util_section,
            text="🛠️ CÔNG CỤ TIỆN ÍCH",
            font=section_font,
            text_color=("#a35cff", "#c084fc"),
        ).pack(pady=(0, 15))

        util_button_frame = ctk.CTkFrame(util_section, fg_color="transparent")
        util_button_frame.pack(fill="x", padx=15, pady=5)
        util_button_frame.grid_columnconfigure(0, weight=1)

        # Modern TDS button with purple gradient
        self.tds_btn = ctk.CTkButton(
            util_button_frame,
            text="🔐 ĐỔI MẬT KHẨU TDS",
            height=65,
            corner_radius=15,
            font=button_font,
            fg_color=("#8b5cf6", "#7c3aed"),
            hover_color=("#7c3aed", "#6d28d9"),
            border_width=2,
            border_color=("#7c3aed", "#a78bfa"),
            text_color=("#ffffff", "#ffffff"),
            command=lambda: self.start_fetch(TDS_URL),
        )
        self.tds_btn.grid(row=0, column=0, padx=15, pady=10, sticky="ew")

        # New DVMXH button with teal gradient
        self.dvmxh_btn = ctk.CTkButton(
            util_button_frame,
            text="🛒 DỊCH VỤ MẠNG XÃ HỘI",
            height=65,
            corner_radius=15,
            font=button_font,
            fg_color=("#14b8a6", "#0d9488"),
            hover_color=("#0d9488", "#0f766e"),
            border_width=2,
            border_color=("#0d9488", "#2dd4bf"),
            text_color=("#ffffff", "#ffffff"),
            command=lambda: self.start_fetch(DVMXH_URL),
        )
        self.dvmxh_btn.grid(row=1, column=0, padx=15, pady=10, sticky="ew")

        # Modern progress bar with glow effect
        self.progress = ctk.CTkProgressBar(
            self.scrollable_frame,
            height=12,
            corner_radius=6,
            progress_color=("#00d4ff", "#00d4ff"),
            fg_color=("#e0e0e0", "#1e2749"),
        )
        self.progress.grid(row=4, column=0, padx=120, pady=(25, 12), sticky="ew")
        self.progress.set(0)

        # Status label with better contrast
        self.status = ctk.CTkLabel(
            self.scrollable_frame,
            text="✨ Sẵn sàng sử dụng",
            font=ctk.CTkFont(family="Segoe UI", size=16),
            text_color=("#00b894", "#00d4aa"),
        )
        self.status.grid(row=5, column=0, padx=50, pady=(0, 25))

        # Modern exit button
        self.exit_btn = ctk.CTkButton(
            self.scrollable_frame,
            text="❌ Thoát ứng dụng",
            height=45,
            corner_radius=12,
            font=ctk.CTkFont(family="Segoe UI", size=15, weight="bold"),
            fg_color=("#dc2626", "#991b1b"),
            hover_color=("#991b1b", "#7f1d1d"),
            border_width=2,
            border_color=("#991b1b", "#dc2626"),
            text_color=("#ffffff", "#ffffff"),
            command=self.destroy,
        )
        self.exit_btn.grid(row=6, column=0, padx=50, pady=(15, 30))  # Properly positioned at the bottom

    # Đã bỏ kiểm tra session/key, không cần check_session

    def set_loading(self, loading: bool, message: str = ""):
        # Disable/enable all action buttons during loading
        buttons = [
            self.action_btn, 
            self.golike_tiktok_btn,
            self.golike_youtube_btn,  # Added new YouTube button
            self.golike_twitter_btn,
            self.golike_linkedin_btn,  # Added new LinkedIn button
            self.golike_ig_btn,
            self.golike_ig_v1_btn,
            self.golike_ig_v2_btn,
            self.golike_btn,
            self.tds_btn,
            self.dvmxh_btn
        ]
        
        for btn in buttons:
            btn.configure(state=("disabled" if loading else "normal"))
            
        if loading:
            self.progress.configure(mode="indeterminate")
            self.progress.start()
            self.status.configure(text_color=("#ff9800", "#ffa94d"))
        else:
            self.progress.stop()
            self.progress.configure(mode="determinate")
            self.progress.set(0)
            self.status.configure(text_color=("#00b894", "#00d4aa"))
        if message:
            self.status.configure(text=f"⏳ {message}" if loading else f"✨ {message}")

    def start_fetch(self, url):
        self.launch_url = url
        self.fetch_and_launch()

    def fetch_and_launch(self):
        self.set_loading(True, "Đang tải module... Vui lòng chờ.")
        self.after(100, self._do_fetch_and_launch)

    def _do_fetch_and_launch(self):
        try:
            url = getattr(self, "launch_url", URL)
            resp = requests.get(url, timeout=25)
            resp.raise_for_status()
            code = resp.text
        except Exception as e:
            self.set_loading(False, "❌ Lỗi khi tải module.")
            messagebox.showerror("Lỗi", f"Không thể tải module:\n{e}")
            return

        try:
            with tempfile.NamedTemporaryFile("w", delete=False, suffix=".py", encoding="utf-8") as f:
                f.write(code)
                tmp_path = f.name

            creationflags = 0
            if sys.platform.startswith("win"):
                creationflags = getattr(subprocess, "CREATE_NEW_CONSOLE", 0)

            subprocess.Popen([sys.executable, tmp_path], creationflags=creationflags)
            self.set_loading(False, "✅ Đã khởi chạy công cụ thành công!")
            messagebox.showinfo(
                "Thành công",
                "✅ Công cụ đã được mở trong cửa sổ mới!\n\n⏳ Vui lòng chờ khoảng 10 giây để công cụ khởi động hoàn tất.\n\n💡 Nếu cửa sổ mới không hiện, hãy kiểm tra thanh taskbar.",
            )
        except Exception as e:
            self.set_loading(False, "❌ Không thể khởi chạy module.")
            messagebox.showerror("Lỗi", f"Không thể khởi chạy module:\n{e}")

def main():
    # Bỏ xác thực key, vào thẳng menu chính
    app = App(user_key=None)
    app.mainloop()

if __name__ == "__main__":
    main()