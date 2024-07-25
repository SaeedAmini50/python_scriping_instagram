import json

# کوکی‌های شما به صورت رشته
cookies_string = """mid=ZpFrbAABAAEGyAIDBdDQOyN6_Olw; ig_did=599CB284-E80B-4D33-B8AC-2075FC890208; dpr=2.8125; datr=Cq2RZve1fEaFZ8_sFHMg3xG5; ps_n=1; ps_l=1; csrftoken=gr85YdJ5cpD08Bd8ei5xuk3WTYDYLQgJ; ds_user_id=67984354232; sessionid=67984354232%3ASzMYiEL5hqagHG%3A5%3AAYfAeQvUU0vCx-DoUVMnaVGZWyQb4tPk9QMkAozw4w; shbid="18042\05467984354232\0541752425896:01f7476e18bed210c56e7b565b980f977a71efc849989697ebd4fca036aff1a3a65368e9"; shbts="1720889896\05467984354232\0541752425896:01f7a66c65b731490f6aea59d7082f7e1e690fa528cce9b0269a8b3541fcbcb142d11784"; wd=384x729; rur="RVA\05467984354232\0541752426064:01f71a011a51971766d77eb38f4a23b971b034bcb96e6ff2d949b65ee0bc94d28dbffb8a"""

# تبدیل رشته کوکی‌ها به دیکشنری
cookies = {}
for cookie in cookies_string.split("; "):
    key, value = cookie.split("=", 1)
    cookies[key] = value

# ذخیره کوکی‌ها به فایل JSON
with open("cookies_from_phone.json", "w") as file:
    json.dump(cookies, file)
