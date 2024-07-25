from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import pandas as pd

def random_sleep(min_time, max_time):
    time.sleep(random.uniform(min_time, max_time))

# تنظیمات مرورگر Chrome و نصب درایور
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # اجرای بدون نمایش مرورگر (اختیاری)

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

pages = ["s_a_1375a"]

# رفتن به صفحه پروفایل بعد از اضافه کردن کوکی‌ها
driver.get("https://www.instagram.com/" + pages[0])

random_sleep(2, 4)

# کلیک بر روی دکمه فالوورها
follower_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href,"/followers/")]')))
follower_button.click()

random_sleep(4, 5)

# استخراج و چاپ یوزرهای فالوورها
user_elements = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@role="dialog"]//a[contains(@href, "/")]/div/div[2]/div[1]')))
usernames = [user.text for user in user_elements if user.text != '']
i = 1
for username in usernames:
    print(f"{i}: {username}")
    i += 1

# ذخیره کردن یوزرها در فایل followers.txt
with open("followers.txt", "w") as file:
    for username in usernames:
        file.write(username + "\n")

print("Usernames saved to followers.txt")

# خواندن یوزرها از فایل followers.txt
with open("followers.txt", "r") as file:
    usernames = file.readlines()
    usernames = [username.strip() for username in usernames]

# ایجاد لیست برای ذخیره اطلاعات فالوورها
followers_info = []

# پیمایش بر روی هر فالوور و دریافت اطلاعات آن
for username in usernames:
    # رفتن به صفحه پروفایل فالوور
    driver.get(f"https://www.instagram.com/{username}/")
    random_sleep(2, 4)
    
    try:
        # استخراج اطلاعات فالوور
        full_name = driver.find_element(By.XPATH, '//h1[contains(@class, "_aacl _aaco _aacu _aacx _aad7 _aade")]').text
        name = driver.find_element(By.XPATH, '//span[contains(@class, "_aacl _aaco _aacu _aacx _aad7 _aade")]').text
        posts = driver.find_element(By.XPATH, '//span[contains(@class, "_ac2a")]').text
        followers = driver.find_element(By.XPATH, '//a[contains(@href,"/followers/")]//span').get_attribute('title')
        following = driver.find_element(By.XPATH, '//a[contains(@href,"/following/")]//span').text

        followers_info.append({
            "username": username,
            "full_name": full_name,
            "name": name,
            "posts": posts,
            "followers": followers,
            "following": following
        })
    except Exception as e:
        print(f"Error fetching info for {username}: {e}")
    
    random_sleep(1, 2)

# ذخیره اطلاعات به صورت جدول در فایل
df = pd.DataFrame(followers_info)
df.to_csv("followers_info.csv", index=False)
print("Followers' information saved to followers_info.csv")

# بستن مرورگر
driver.quit()
