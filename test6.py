import json
from instagrapi import Client

# لیست کوکی‌های شما
cookies_list = [
    {"domain": ".instagram.com", "expiry": 1721660542, "httpOnly": False, "name": "wd", "path": "/", "sameSite": "Lax", "secure": True, "value": "1036x506"},
    {"domain": ".instagram.com", "httpOnly": True, "name": "rur", "path": "/", "sameSite": "Lax", "secure": True, "value": "\"RVA\\05467984354232\\0541752591732:01f76ec1a43715f2a81580321e1164241da2a4419f39b5c19cedf3a7ea1a4695c4fa392d\""},
    {"domain": "www.instagram.com", "httpOnly": False, "name": "wd", "path": "/", "sameSite": "Lax", "secure": True, "value": "384x729"},
    {"domain": "www.instagram.com", "httpOnly": False, "name": "sessionid", "path": "/", "sameSite": "Lax", "secure": True, "value": "67984354232%3AJagstbmtGmp1Q5%3A12%3AAYfvv8fyygQ2J-66G8nC7C6Yz04ljwADNZK-gw_AYg"},
    {"domain": "www.instagram.com", "httpOnly": False, "name": "mid", "path": "/", "sameSite": "Lax", "secure": True, "value": "ZpOTVgABAAFzETY_Kgx6fgKMbZHm"},
    {"domain": "www.instagram.com", "httpOnly": False, "name": "ds_user_id", "path": "/", "sameSite": "Lax", "secure": True, "value": "67984354232"},
    {"domain": "www.instagram.com", "httpOnly": False, "name": "rur", "path": "/", "sameSite": "Lax", "secure": True, "value": "\"RVA\\05467984354232\\0541752588901:01f72fecfbe7d2c4c155d2cc3dfd651acb304035a89ef18c73cedb3c76b71b69c7cf0f70\""},
    {"domain": "www.instagram.com", "httpOnly": False, "name": "ig_nrcb", "path": "/", "sameSite": "Lax", "secure": True, "value": "1"},
    {"domain": ".instagram.com", "expiry": 1721660542, "httpOnly": False, "name": "dpr", "path": "/", "sameSite": "None", "secure": True, "value": "1.5"},
    {"domain": "www.instagram.com", "httpOnly": False, "name": "csrftoken", "path": "/", "sameSite": "Lax", "secure": True, "value": "OHB2Y6s9wRRnPwmgrr4br4t6NzSGghdR"},
    {"domain": ".instagram.com", "expiry": 1752505332, "httpOnly": False, "name": "csrftoken", "path": "/", "sameSite": "Lax", "secure": True, "value": "OHB2Y6s9wRRnPwmgrr4br4t6NzSGghdR"},
    {"domain": "www.instagram.com", "httpOnly": False, "name": "datr", "path": "/", "sameSite": "Lax", "secure": True, "value": "VpOTZq7F4qmLZBotlBtd9Kbq"},
    {"domain": "www.instagram.com", "httpOnly": False, "name": "shbts", "path": "/", "sameSite": "Lax", "secure": True, "value": "\"1720947722\\05467984354232\\0541752483722:01f7889bb04ebe3cdb26af1418f7383b48fde45dd94d915fa21cc8e9d0e85ca37828d016\""},
    {"domain": "www.instagram.com", "httpOnly": False, "name": "shbid", "path": "/", "sameSite": "Lax", "secure": True, "value": "\"18042\\05467984354232\\0541752483722:01f739f694198f1b76f7632b1b23a55765928c0acc511f4bfcb939d81e2b8d467cc5cd43\""},
    {"domain": "www.instagram.com", "httpOnly": False, "name": "ig_did", "path": "/", "sameSite": "Lax", "secure": True, "value": "FC4DB20E-D1D0-47B3-AA46-3CCE2C98A5C1"},
    {"domain": ".instagram.com", "expiry": 1728831732, "httpOnly": False, "name": "ds_user_id", "path": "/", "sameSite": "Lax", "secure": True, "value": "67984354232"},
    {"domain": "www.instagram.com", "httpOnly": False, "name": "dpr", "path": "/", "sameSite": "Lax", "secure": True, "value": "2.8125"}
]

# متغیر USER_AGENT را تعریف کنید
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# تبدیل لیست کوکی‌ها به دیکشنری
cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies_list}

# ساختار دیکشنری تنظیمات
settings_dict = {
    "authorization_data": {},
    "cookies": cookies_dict,
    "user_agent": USER_AGENT,
    "country": "US",
    "locale": "en_US",
    "device_settings": {
        "manufacturer": "Google",
        "model": "Pixel 3",
        "android_version": 28,
        "android_release": "9.0"
    }
}

# ذخیره به عنوان فایل JSON
with open("instagram_settings.json", "w") as file:
    json.dump(settings_dict, file)

print("Settings dictionary saved to 'instagram_settings.json'")

# تابع برای بارگذاری کوکی‌ها
def load_cookies(client, filepath):
    with open(filepath, 'r') as file:
        settings = json.load(file)
    client.set_settings(settings)
    client.set_csrf_token(settings['cookies']['csrftoken'])
    return True

# ایجاد شیء Client
cl = Client()

# مسیر فایل JSON تنظیمات
COOKIES_FILE = 'instagram_settings.json'

# بارگذاری کوکی‌ها
if load_cookies(cl, COOKIES_FILE):
    print("Cookies loaded successfully")
else:
    print("Failed to load cookies")
