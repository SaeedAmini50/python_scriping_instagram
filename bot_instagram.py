from instabot import Bot
import time
import os
import glob



# حذف فایل‌های کوکی و نشست
for filename in glob.glob("config/*cookie.json"):
    os.remove(filename)
for filename in glob.glob("config/*uuid_and_cookie.json"):
    os.remove(filename)

my_bot = Bot()


my_bot.login(username="instascript2024", password="script")
time.sleep(5) 
my_bot.follow("s_a_1375a")


time.sleep(30) 

followers_list=my_bot.get_user_followers("s_a_1375a")

following_list=my_bot.get_user_following("s_a_1375a")


for count,each_follower in followers_list:
    if count > 4:
        continue
    time.sleep(5)
    print(my_bot.get_username_from_user_id(each_follower))


for count,each_follow in following_list:
    if count > 4:
        continue
    time.sleep(5)
    print(my_bot.get_username_from_user_id(each_follower))


my_bot.logout()