from instagrapi import Client
import time
import json
import os
import random

# تابع برای بارگذاری کوکی‌ها
def load_cookies(client, filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            settings = json.load(file)
            client.set_settings(settings)
            print("کوکی‌ها با موفقیت بارگذاری شدند.")
        return True
    else:
        print("فایل کوکی‌ها پیدا نشد.")
        return False

# تابع برای بارگذاری لیست پروکسی‌ها از فایل
def load_proxies(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            proxies = file.readlines()
        proxies = [proxy.strip() for proxy in proxies if proxy.strip()]
        if proxies:
            return proxies
        else:
            print("پروکسی در فایل یافت نشد.")
            return None
    else:
        print("فایل پروکسی‌ها پیدا نشد.")
        return None

# ایجاد شیء Client
print("ایجاد شیء Client...")
cl = Client()

# بارگذاری کوکی‌ها
cookies_file = "auth_data.json"
if load_cookies(cl, cookies_file):
    print("استفاده از کوکی‌های بارگذاری شده برای ورود به حساب کاربری...")
else:
    print("ورود به حساب کاربری...")
    cl.login("s_a_1375a", "amini1375")
    print("ورود با موفقیت انجام شد!")

# بارگذاری و تنظیم پروکسی
proxies_file = "list_of_proxy.txt"
proxies = load_proxies(proxies_file)
if proxies:
    selected_proxy = random.choice(proxies)
    cl.set_proxy(selected_proxy)  # رشته URL پروکسی را به عنوان ورودی بدهید
    print(f"استفاده از پروکسی: {selected_proxy}")

# دریافت لیست فالوورها
print("در حال دریافت فالوورها...")
time.sleep(10)
try:
    user_id = cl.user_id_from_username("instascript2024")
    followers = cl.user_followers(user_id)
    print(f"مجموع فالوورهای دریافت شده: {len(followers)}")

    # چاپ لیست فالوورها
    print("چاپ فالوورها:")
    for follower_id, follower_info in followers.items():
        time.sleep(2)
        print(f"نام کاربری: {follower_info.username}, نام کامل: {follower_info.full_name}")
except Exception as e:
    print(f"خطا: {e}")

# خروج از حساب کاربری
print("خروج از حساب کاربری...")
cl.logout()
print("خروج با موفقیت انجام شد!")

