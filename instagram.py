from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import json
import tkinter as tk
from tkinter import messagebox


def random_sleep(min_time=2, max_time=5):
    time.sleep(random.uniform(min_time, max_time))


def scrape_instagram_hashtag(hashtag, num_posts, username, password):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # اجرای بدون نمایش مرورگر (اختیاری)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://www.instagram.com/accounts/login/")
    random_sleep()

    # ورود به حساب کاربری
    driver.find_element(By.NAME, "username").send_keys(username)
    random_sleep()
    driver.find_element(By.NAME, "password").send_keys(password)
    random_sleep()
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    random_sleep(5, 7)

    # جستجوی هشتگ
    driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
    random_sleep(5, 7)

    # اسکرپینگ پست‌ها
    posts = []
    while len(posts) < num_posts:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        random_sleep(3, 5)
        elements = driver.find_elements(By.CSS_SELECTOR, "div.v1Nh3 a")
        posts.extend([element.get_attribute("href") for element in elements])
        posts = list(set(posts))  # حذف لینک‌های تکراری

    # محدود کردن تعداد پست‌ها
    posts = posts[:num_posts]

    posts_data = []
    for post_url in posts:
        driver.get(post_url)
        random_sleep(3, 5)

        try:
            date = driver.find_element(By.CSS_SELECTOR, "time._1o9PC").get_attribute("datetime")
            likes = driver.find_element(By.CSS_SELECTOR, "div.Nm9Fw span").text
            comments = len(driver.find_elements(By.CSS_SELECTOR, "ul.Mr508"))
            caption = driver.find_element(By.CSS_SELECTOR, "div.C4VMK span").text
        except Exception as e:
            print(f"Error fetching data for {post_url}: {e}")
            continue

        posts_data.append({
            "date": date,
            "likes": likes,
            "comments": comments,
            "caption": caption,
            "url": post_url,
        })

    driver.quit()

    # نمایش اطلاعات در کنسول
    for i, post in enumerate(posts_data[:num_posts]):
        print(f"Post {i + 1}:")
        print(f"Date: {post['date']}")
        print(f"Likes: {post['likes']}")
        print(f"Comments: {post['comments']}")
        print(f"Caption: {post['caption']}")
        print(f"URL: {post['url']}")
        print("-" * 50)

    return posts_data


def on_submit():
    hashtag = hashtag_entry.get()
    num_posts = 10  # تعداد پست‌ها را به 10 محدود کنید
    username = username_entry.get()
    password = password_entry.get()
    try:
        posts_data = scrape_instagram_hashtag(hashtag, num_posts, username, password)
        messagebox.showinfo("Success", f"Data displayed in console.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI setup
root = tk.Tk()
root.title("Instagram Hashtag Scraper")

tk.Label(root, text="Hashtag").grid(row=0)
tk.Label(root, text="Instagram Username").grid(row=1)
tk.Label(root, text="Instagram Password").grid(row=2)

hashtag_entry = tk.Entry(root)
username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show='*')

hashtag_entry.grid(row=0, column=1)
username_entry.grid(row=1, column=1)
password_entry.grid(row=2, column=1)

tk.Button(root, text='Submit', command=on_submit).grid(row=3, column=1, sticky=tk.W, pady=4)

root.mainloop()
