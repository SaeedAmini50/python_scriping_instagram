from instagrapi import Client

# تبدیل کوکی‌ها به دیکشنری
def cookies_to_dict(cookies):
    return {cookie['name']: cookie['value'] for cookie in cookies}

# کوکی‌ها را از خروجی selenium بگیرید و در اینجا جایگزین کنید
cookies = [
    {'domain': '.instagram.com', 'expiry': 1755714375, 'httpOnly': False, 'name': 'mid', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'Zpa7QAALAAEbBGtLCuWbGW8CZXHr'},
    {'domain': '.instagram.com', 'expiry': 1721759174, 'httpOnly': False, 'name': 'dpr', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1.5'},
    {'domain': '.instagram.com', 'expiry': 1721759174, 'httpOnly': False, 'name': 'wd', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '1036x506'},
    {'domain': '.instagram.com', 'expiry': 1752690371, 'httpOnly': False, 'name': 'ig_nrcb', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '1'},
    {'domain': '.instagram.com', 'expiry': 1755714375, 'httpOnly': True, 'name': 'datr', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'QLuWZnPkTgUR-VuJqUzuYZ32'},
    {'domain': '.instagram.com', 'expiry': 1752690375, 'httpOnly': True, 'name': 'ig_did', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1EC091E0-883C-4E0E-9AF0-5FC786A5A35C'},
    {'domain': '.instagram.com', 'expiry': 1752603971, 'httpOnly': False, 'name': 'csrftoken', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'qnGaTrjMPeZwoQKaFG8ywM'},
    {'domain': '.instagram.com', 'expiry': 1755714375, 'httpOnly': True, 'name': 'sessionid', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '67984354232%3AoTFXgfh0tcmVdX%3A18%3AAYeI2aqYgFw1OTZOUA2ZzIOlrC4uM0cNbgSzIglKzA'},  # اینجا باید کوکی sessionid اضافه شود
    {'domain': '.instagram.com', 'expiry': 1752603971, 'httpOnly': False, 'name': 'ds_user_id', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '67984354232'}  # اینجا باید کوکی ds_user_id اضافه شود
]

# تبدیل کوکی‌ها به دیکشنری
cookie_dict = cookies_to_dict(cookies)

# ورود با استفاده از کوکی‌ها
client = Client()
client.login_by_sessionid(cookie_dict['sessionid'])
