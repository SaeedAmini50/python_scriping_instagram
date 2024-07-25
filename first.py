from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def random_sleep(min_time, max_time):
    time.sleep(random.uniform(min_time, max_time))

# تنظیمات مرورگر Chrome و نصب درایور
options = webdriver.ChromeOptions()
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
options.add_argument(f"user-agent={USER_AGENT}")
# options.add_argument("--headless")  # اجرای بدون نمایش مرورگر (اختیاری)

# ایجاد شیء مرورگر با استفاده از ChromeDriverManager برای مدیریت درایور
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# باز کردن صفحه اینستاگرام
driver.get("https://www.instagram.com")

# افزودن کوکی‌ها
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

for cookie in cookies:
    driver.add_cookie(cookie)

# باز کردن دوباره صفحه اینستاگرام برای اعمال کوکی‌ها
driver.get("https://www.instagram.com")
random_sleep(3, 5)

# ورود به حساب کاربری
username = "saeedamini.insta"
password = "saeed1375"

# پیدا کردن و وارد کردن نام کاربری
try:
    username_input = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.NAME, "username")))
    username_input.send_keys(username)
except:
    print("Error: username input field not found.")
    driver.quit()

# پیدا کردن و وارد کردن رمز عبور
try:
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(password)
except:
    print("Error: password input field not found.")
    driver.quit()

# کلیک بر روی دکمه ورود
try:
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
except:
    print("Error: login button not found.")
    driver.quit()

# منتظر شدن برای ورود و بارگذاری صفحه اصلی
try:
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Home')]")))
except:
    print("Error: Home element not found.")
    driver.quit()

# رفتن به صفحه پروفایل
profile_url = "https://www.instagram.com/" + username + "/"
driver.get(profile_url)

random_sleep(2, 4)

# کلیک بر روی دکمه فالوورها
try:
    follower_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href,"/followers/")]')))
    follower_button.click()
except:
    print("Error: follower button not found.")
    driver.quit()

random_sleep(4, 5)

# خروج از حساب کاربری پس از دو دقیقه
time.sleep(120)
try:
    profile_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@aria-label='Profile']")))
    profile_button.click()
except:
    print("Error: profile button not found.")
    driver.quit()

random_sleep(2, 4)

try:
    logout_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Log Out')]")))
    logout_button.click()
except:
    print("Error: logout button not found.")
    driver.quit()

driver.quit()
