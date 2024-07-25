from instagrapi import Client
import time
import json
import os

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

# ایجاد شیء Client
print("Creating Client object...")
cl = Client()

# بارگذاری کوکی‌ها
cookies_file = "instagram_cookies2.json"
if load_cookies(cl, cookies_file):
    print("Using loaded cookies for login...")
else:
    # ورود به حساب کاربری اینستاگرام در صورت نبود کوکی‌ها
    print("Logging in...")
    cl.login("instascript2024", "script")
    print("Logged in successfully!")

# دریافت لیست فالوورها
print("Fetching followers...")
time.sleep(10)
user_id = cl.user_id_from_username("s_a_1375a")
followers = cl.user_followers(user_id)
print(f"Total followers fetched: {len(followers)}")

# چاپ لیست فالوورها
print("Printing followers:")
for follower_id, follower_info in followers.items():
    time.sleep(2)
    print(f"Username: {follower_info.username}, Full Name: {follower_info.full_name}")

# خروج از حساب کاربری
print("Logging out...")
cl.logout()
print("Logged out successfully!")
