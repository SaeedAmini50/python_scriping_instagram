from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def login_and_get_cookies(username, password):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(5)
    
    # وارد کردن نام کاربری و رمز عبور
    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')
    
    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    
    time.sleep(5)  # زمان انتظار برای لاگین شدن
    
    # استخراج کوکی‌ها
    cookies = driver.get_cookies()
    driver.quit()
    
    return cookies

username = 'saeedamini.insta@gmail.com'
password = 'saeed1375'
cookies = login_and_get_cookies(username, password)
print(cookies)
