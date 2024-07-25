from instagrapi import Client
import os
import time
import json

# نام فایل کوکی‌ها
COOKIES_FILE = "instagram3.json"

def save_cookies(client, filename):
    with open(filename, 'w') as file:
        json.dump(client.get_settings(), file)

def load_cookies(client, filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            settings = json.load(file)
            client.set_settings(settings)

# ایجاد شیء Clientشسط
print("Creating Client object...")
cl = Client()

# تلاش برای بارگذاری کوکی‌ها
print("Loading cookies...")
load_cookies(cl, COOKIES_FILE)

# چک کردن وضعیت ورود
if not cl.user_id:
    print("Logging in...")
    cl.login("s_a_1375a", "amini1375")
    print("Logged in successfully!")
    # ذخیره کوکی‌ها بعد از ورود
    save_cookies(cl, COOKIES_FILE)
else:
    print("Logged in using cookies!")

# خروج از حساب کاربری
print("Logging out...")
cl.logout()
print("Logged out successfully!")
