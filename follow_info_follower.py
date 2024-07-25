from instagrapi import Client
import time
import random
import json
import os
import pandas as pd

# اطلاعات حساب کاربری
USERNAME = "cordia4412024"
PASSWORD = "amini66"
TARGET_USERNAME = "s_a_1375a"
COOKIES_FILE = "instagram_cookies4.json"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

def random_delay(min_time=1.0, max_time=3.0):
    """ایجاد تأخیر تصادفی"""
    delay = random.uniform(min_time, max_time)
    print(f"Sleeping for {delay:.2f} seconds...")
    time.sleep(delay)

# تابع برای بارگذاری کوکی‌ها
def load_cookies(client, filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            settings = json.load(file)
            client.set_settings(settings)
            print("Cookies loaded successfully.")
        return True
    else:
        print("Cookies file not found.")
        return False

# تابع برای ذخیره کوکی‌ها
def save_cookies(client, filename):
    with open(filename, 'w') as file:
        json.dump(client.get_settings(), file)
    print(f"Cookies saved to {filename}")

# ایجاد شیء Client
print("Creating Client object...")
cl = Client()

# تنظیم User-Agent
cl.set_user_agent(USER_AGENT)
print(f"User-Agent set to: {USER_AGENT}")
random_delay()

# بارگذاری کوکی‌ها
if load_cookies(cl, COOKIES_FILE):
    print("Using loaded cookies for login...")
else:
    # ورود به حساب کاربری اینستاگرام در صورت نبود کوکی‌ها
    print("Logging in...")
    cl.login(USERNAME, PASSWORD)
    print("Logged in successfully!")

# خروج از حساب کاربری
print("Logging out...")
cl.logout()
print("Logged out successfully!")
random_delay()
