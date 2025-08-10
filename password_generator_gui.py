import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    """توليد كلمة المرور وعرضها في الواجهة"""
    try:
        length = int(length_entry.get())
        if length < 6:
            messagebox.showerror(
                "خطأ", "طول كلمة المرور يجب أن يكون على الأقل 6 أحرف.")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_var.set(password)
    except ValueError:
        messagebox.showerror("خطأ", "من فضلك أدخل رقم صحيح.")


def copy_to_clipboard():
    """نسخ كلمة المرور إلى الحافظة"""
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("تم النسخ", "تم نسخ كلمة المرور إلى الحافظة!")


# إعداد الواجهة
root = tk.Tk()
root.title("🔐 مولد كلمات مرور آمنة")
root.geometry("400x250")
root.resizable(False, False)

# طول كلمة المرور
tk.Label(root, text="أدخل طول كلمة المرور:", font=("Arial", 12)).pack(pady=10)
length_entry = tk.Entry(root, font=("Arial", 12), justify="center")
length_entry.pack()

# زر التوليد
tk.Button(root, text="توليد كلمة المرور", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
          command=generate_password).pack(pady=10)

# عرض كلمة المرور
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, font=("Arial", 12),
         justify="center", state="readonly").pack()

# زر النسخ
tk.Button(root, text="نسخ كلمة المرور", font=("Arial", 12), bg="#2196F3", fg="white",
          command=copy_to_clipboard).pack(pady=10)

root.mainloop()
