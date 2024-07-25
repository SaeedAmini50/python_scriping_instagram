from instagrapi import Client
import json
import os

# اطلاعات حساب کاربری
TARGET_USERNAME = "instascript2024"
ACCESS_TOKEN = "IGQWRQWk9DU1h6TVZAhVmdtMk9iQmNORXBEcVBRajJBSTVEU3E4anJFT3B6N2xPYnVJeVpHeENTZAnI2R1VLVExRdWFhbExCMlhKLTNTX2FOU0VqVV9pdGl0Y3M5Yk5UUHpKVjl4ZA252UmpWRUVIMnlacnoyTk5vSzAZD"
COOKIES_FILE = "instagram_cookies2.json"

# تابع برای بارگذاری کوکی‌ها
def load_cookies(client, filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            settings = json.load(file)
            if isinstance(settings, list):
                settings = settings[0]  # اگر یک لیست بود، اولین عنصر را به عنوان تنظیمات در نظر بگیر
            client.set_settings(settings)
            print("Cookies loaded successfully.")
        return True
    else:
        print("Cookies file not found.")
        return False

# تابع برای ذخیره کوکی‌ها
def save_cookies(client, filename):
    with open(filename, 'w') as file:
        json.dump([client.get_settings()], file)  # تنظیمات را به صورت یک لیست ذخیره کن
    print(f"Cookies saved to {filename}")

# ایجاد شیء Client
cl = Client()

# بارگذاری کوکی‌ها
if load_cookies(cl, COOKIES_FILE):
    print("Using loaded cookies for login...")
else:
    # ورود به حساب کاربری اینستاگرام در صورت نبود کوکی‌ها
    cl.login_by_access_token(ACCESS_TOKEN)
    print("Logged in successfully!")
    # ذخیره کوکی‌ها
    save_cookies(cl, COOKIES_FILE)

# دریافت ID کاربر هدف
print(f"Fetching user ID for {TARGET_USERNAME}...")
target_user_id = cl.user_id_from_username(TARGET_USERNAME)
if target_user_id:
    print(f"User ID for {TARGET_USERNAME}: {target_user_id}")

    # دریافت فالوورها
    print(f"Fetching followers for user ID {target_user_id}...")
    followers = cl.user_followers(target_user_id, amount=10)
    if followers:
        print(f"Total followers fetched: {len(followers)}")
        for follower_id, follower_info in followers.items():
            print(f"Username: {follower_info.username}, Full Name: {follower_info.full_name}")
else:
    print(f"Failed to fetch user ID for {TARGET_USERNAME}.")

# خروج از حساب کاربری
cl.logout()
print("Logged out successfully!")
