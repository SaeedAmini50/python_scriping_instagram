from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# تنظیمات مرورگر Chrome و نصب درایور
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0")

# ایجاد شیء مرورگر با استفاده از ChromeDriverManager برای مدیریت درایور
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# باز کردن صفحه اینستاگرام
driver.get("https://www.instagram.com")
time.sleep(5)

# اضافه کردن کوکی‌ها به مرورگر
cookies = [
    {"name": "mid", "value": "ZpFrbAABAAEGyAIDBdDQOyN6_Olw", "domain": ".instagram.com"},
    {"name": "ig_did", "value": "599CB284-E80B-4D33-B8AC-2075FC890208", "domain": ".instagram.com"},
    {"name": "dpr", "value": "2.8125", "domain": ".instagram.com"},
    {"name": "datr", "value": "Cq2RZve1fEaFZ8_sFHMg3xG5", "domain": ".instagram.com"},
    {"name": "ps_n", "value": "1", "domain": ".instagram.com"},
    {"name": "ps_l", "value": "1", "domain": ".instagram.com"},
    {"name": "csrftoken", "value": "3CkJ3H9pLNfdXHoCz3EdD1hy9MfBQHol", "domain": ".instagram.com"},
    {"name": "ds_user_id", "value": "67984354232", "domain": ".instagram.com"},
    {"name": "sessionid", "value": "67984354232%3AIMDQySk9FXC84K%3A2%3AAYcpKr2E6PuoArjuX6U11DSraHd94GnU_CrKHrHU0Q", "domain": ".instagram.com"},
    {"name": "shbid", "value": '18042\\05467984354232\\0541752425896:01f7476e18bed210c56e7b565b980f977a71efc849989697ebd4fca036aff1a3a65368e9', "domain": ".instagram.com"},
    {"name": "shbts", "value": '1720889896\\05467984354232\\0541752425896:01f7a66c65b731490f6aea59d7082f7e1e690fa528cce9b0269a8b3541fcbcb142d11784', "domain": ".instagram.com"},
    {"name": "wd", "value": "384x729", "domain": ".instagram.com"},
    {"name": "rur", "value": 'RVA\\05467984354232\\0541752474477:01f75aec0f512190695aa7bc0df98b60ce125c3b214ee9589174eac9c170dbaa6c8a323f', "domain": ".instagram.com"}
]

for cookie in cookies:
    driver.add_cookie(cookie)

# تأخیر برای اطمینان از بارگذاری کامل صفحه
time.sleep(2)

# باز کردن دوباره صفحه اینستاگرام برای اعمال کوکی‌ها
driver.get("https://www.instagram.com")
time.sleep(5)

# بررسی ورود به حساب کاربری
try:
    driver.find_element(By.XPATH, "//span[@aria-label='Profile']")
    print("Login successful!")
except:
    print("Login failed!")
# بررسی ورود به حساب کاربری
print("1")
time.sleep(5)
print("2")
time.sleep(5)
  