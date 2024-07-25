from instagrapi import Client
from requests.cookies import cookiejar_from_dict
import requests

# کوکی‌ها را به شکل دیکشنری درآورید
cookies = [
    {'name': 'csrftoken', 'value': 'wEwnHZY9vH5fKF4Y2UBgYNiNeIH56B8e', 'domain': '.instagram.com', 'path': '/', 'expiry': 1753075954},
    {'name': 'datr', 'value': 'VZWcZqlGOfAOsJiQ2y5-Gj8u', 'domain': '.instagram.com', 'path': '/', 'expiry': 1753073962},
    {'name': 'ds_user_id', 'value': '67984354232', 'domain': '.instagram.com', 'path': '/', 'expiry': 1721537962},
    {'name': 'ig_did', 'value': '9A814DBC-54AF-483F-B6E3-613CE5C892C1', 'domain': '.instagram.com', 'path': '/', 'expiry': 1753075954},
    {'name': 'ig_nrcb', 'value': '1', 'domain': '.instagram.com', 'path': '/', 'expiry': 1753075954},
    {'name': 'mid', 'value': 'ZpyVVwALAAEe-rDzo_As2KZM7seH', 'domain': '.instagram.com', 'path': '/', 'expiry': 1753075954},
    {'name': 'ps_l', 'value': '1', 'domain': '.instagram.com', 'path': '/', 'expiry': 1753075954},
    {'name': 'ps_n', 'value': '1', 'domain': '.instagram.com', 'path': '/', 'expiry': 1753075954},
    {'name': 'rur', 'value': 'CLN\05467984354232\0541753075954:01f71af245f2484db06f8091e2996209f4eef7226317a737aa0533113e154d83b68d96d6', 'domain': '.instagram.com', 'path': '/'},
    {'name': 'sessionid', 'value': '67984354232%3A2V4R9McQtQ4zKS%3A2%3AAYfDEMC7XxX85KWkGYTDFFpc216-x3rl2ED0BSfzSA', 'domain': '.instagram.com', 'path': '/', 'expiry': 1753075954},
    {'name': 'shbid', 'value': '18042\05467984354232\0541753073962:01f70bc48a9e3e0c335f1cc154358ab9a3293e9b14076a148b4e4b5fde2db26716088716', 'domain': '.instagram.com', 'path': '/', 'expiry': 1753073962},
    {'name': 'shbts', 'value': '1721537962\05467984354232\0541753073962:01f79093ea017d7767b29784b1fcf875052a0da97c80f7fe48d619ce708db85f1b523e5f', 'domain': '.instagram.com', 'path': '/', 'expiry': 1753073962},
    {'name': 'wd', 'value': '1358x354', 'domain': '.instagram.com', 'path': '/', 'expiry': 1753075954}
]

# تبدیل لیست کوکی‌ها به دیکشنری
cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}

# ایجاد شیء Client
client = Client()

# تنظیم کوکی‌ها
client.private.cookies = cookiejar_from_dict(cookies_dict, cookiejar=None)

# تست ورود با کوکی‌ها
try:
    user_info = client.user_info(username='your_username')  # نام کاربری خود را وارد کنید
    print(f"Logged in as: {user_info.username}")
except Exception as e:
    print(f"Login failed: {e}")
