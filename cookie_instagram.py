from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import json
from instagrapi import Client
import pandas as pd

def random_sleep(min_time, max_time):
    time.sleep(random.uniform(min_time, max_time))

# تنظیمات مرورگر Chrome و نصب درایور
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # اجرای بدون نمایش مرورگر (اختیاری)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0")

# ایجاد شیء مرورگر با استفاده از ChromeDriverManager برای مدیریت درایور
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# باز کردن صفحه اینستاگرام
driver.get("https://www.instagram.com")

# اضافه کردن کوکی‌ها به مرورگر
cookies = [
    {"name": "mid", "value": "ZldhhAALAAF-7gV6vCGU3KGP1nlo", "domain": ".instagram.com"},
    {"name": "ig_did", "value": "0C038DB6-B2BB-4CDD-970C-20C406BCCE39", "domain": ".instagram.com"},
    {"name": "datr", "value": "i2FXZprx2SPdIPHEuWn2mKQi", "domain": ".instagram.com"},
    {"name": "dpr", "value": "1.5", "domain": ".instagram.com"},
    {"name": "ps_n", "value": "1", "domain": ".instagram.com"},
    {"name": "ps_l", "value": "1", "domain": ".instagram.com"},
    {"name": "ig_nrcb", "value": "1", "domain": ".instagram.com"},
    {"name": "ds_user_id", "value": "66089215806", "domain": ".instagram.com"},
    {"name": "csrftoken", "value": "NhsnngGYOu8uWWMh1kpXDA84BxcJnz9L", "domain": ".instagram.com"},
    {"name": "shbid", "value": '16260\05466089215806\0541751822807:01f7f67a2b674606a702bd089b54f9dc7e85cff8ab5e5b97bbbbf6418023aff7f6e02541', "domain": ".instagram.com"},
    {"name": "shbts", "value": '1720286807\05466089215806\0541751822807:01f77ec259a28d21bd018b4438ba52ab0248a9c85e56ad28188caa3628e2be3074b7309a', "domain": ".instagram.com"},
    {"name": "sessionid", "value": "66089215806%3A5oFl0yoTOsuYKw%3A20%3AAYeeF8YlrTF5GNHs1waz1ESOXVrvOlCG-Jd41i651A", "domain": ".instagram.com"},
    {"name": "wd", "value": "1272x192", "domain": ".instagram.com"},
    {"name": "rur", "value": 'NCG\05466089215806\0541751868922:01f7a1365beed111aaa0ed7f24a70467f1eb519ebc89f4aa417664e32978843f798e2597', "domain": ".instagram.com"}
]

for cookie in cookies:
    driver.add_cookie(cookie)

# تأخیر تصادفی برای اطمینان از بارگذاری کامل صفحه
random_sleep(2, 4)

# ذخیره کوکی‌ها در یک فایل
cookies = driver.get_cookies()
with open("instagram_cookies2.json", "w") as file:
    json.dump(cookies, file)

# بستن مرورگر
driver.quit()

# استفاده از instagrapi برای دریافت اطلاعات فالوورها
USERNAME = "s_a_1375a"
PASSWORD = "amini1375"
TARGET_USERNAME = "instascript2024"

def load_cookies_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def set_cookies_for_client(client, cookies):
    settings = client.get_settings()
    settings['cookies'] = {cookie['name']: {'value': cookie['value'], 'domain': cookie['domain']} for cookie in cookies}
    client.set_settings(settings)

# ایجاد شیء Client
cl = Client()

# بارگذاری و تنظیم کوکی‌ها
cookies = load_cookies_from_file("instagram_cookies2.json")
set_cookies_for_client(cl, cookies)

# دریافت لیست فالوورهای کاربر مورد نظر
try:
    print(f"Fetching followers of {TARGET_USERNAME}...")
    user_id = cl.user_id_from_username(TARGET_USERNAME)
    followers = cl.user_followers(user_id, amount=3)
    print(f"Total followers fetched: {len(followers)}")
except Exception as e:
    print(f"Error fetching followers: {e}")
    cl.logout()
    exit()

# جمع‌آوری اطلاعات ۵ فالوور اول
data = []
for follower_id, follower_info in followers.items():
    try:
        follower_info = cl.user_info(follower_id)
        data.append({
            "username": follower_info.username,
            "full_name": follower_info.full_name,
            "biography": follower_info.biography,
            "profile_pic_url": follower_info.profile_pic_url,
            "is_private": follower_info.is_private,
            "media_count": follower_info.media_count,
            "follower_count": follower_info.follower_count,
            "following_count": follower_info.following_count
        })
        random_sleep(1, 2)
    except Exception as e:
        print(f"Error fetching info for follower {follower_id}: {e}")

# ذخیره اطلاعات به صورت جدول در فایل
df = pd.DataFrame(data)
df.to_csv("followers_info.csv", index=False)
print("Followers' information saved to followers_info.csv")

# خروج از حساب کاربری
cl.logout()
print("Logged out successfully!")
