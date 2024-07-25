import json
import base64

# مقادیر کوکی‌ها
sessionid = "66089215806%3A5oFl0yoTOsuYKw%3A20%3AAYeeF8YlrTF5GNHs1waz1ESOXVrvOlCG-Jd41i651A"
csrftoken = "NhsnngGYOu8uWWMh1kpXDA84BxcJnz9L"
ds_user_id = "66089215806"

# ایجاد رشته ترکیبی
combined_string = f"{sessionid},{csrftoken},{ds_user_id}"

# ایجاد دیکشنری
auth_dict = {
    "sessionid": sessionid,
    "csrftoken": csrftoken,
    "ds_user_id": ds_user_id,
    "should_use_header_over_cookies": True,
    "combined_string": combined_string
}

# تبدیل دیکشنری به رشته JSON
auth_json = json.dumps(auth_dict)

# انکد کردن JSON به ASCII
ascii_encoded = auth_json.encode('ascii')

# تبدیل بایت‌های ASCII به base64
base64_encoded = base64.b64encode(ascii_encoded)

# دیکد کردن base64 به رشته
base64_string = base64_encoded.decode('ascii')

# چاپ نتیجه نهایی
print("Base64 Encoded String:")
print(base64_string)

# برای دیکد کردن از base64 به JSON
decoded_bytes = base64.b64decode(base64_string)
decoded_string = decoded_bytes.decode('ascii')
decoded_dict = json.loads(decoded_string)

# چاپ دیکشنری دیکد شده
print("Decoded JSON Dictionary:")
print(decoded_dict)

# ذخیره کردن رشته base64 در یک فایل
with open("encoded_token.txt", "w") as file:
    file.write(base64_string)

# خواندن از فایل و دیکد کردن دوباره
with open("encoded_token.txt", "r") as file:
    encoded_token_from_file = file.read()

decoded_bytes_from_file = base64.b64decode(encoded_token_from_file)
decoded_string_from_file = decoded_bytes_from_file.decode('ascii')
decoded_dict_from_file = json.loads(decoded_string_from_file)

# چاپ دیکشنری دیکد شده از فایل
print("Decoded JSON Dictionary from File:")
print(decoded_dict_from_file)



"""import json
import base64

# مقادیر کوکی‌ها
sessionid = "66089215806%3A5oFl0yoTOsuYKw%3A20%3AAYeeF8YlrTF5GNHs1waz1ESOXVrvOlCG-Jd41i651A"
csrftoken = "NhsnngGYOu8uWWMh1kpXDA84BxcJnz9L"
ds_user_id = "66089215806"

# ایجاد رشته ترکیبی
combined_string = f"{sessionid},{csrftoken},{ds_user_id}"

# ایجاد دیکشنری
auth_dict = {
    "sessionid": sessionid,
    "csrftoken": csrftoken,
    "ds_user_id": ds_user_id,
    "should_use_header_over_cookies": True,
    "combined_string": combined_string
}

# تبدیل دیکشنری به رشته JSON
auth_json = json.dumps(auth_dict)

# انکد کردن JSON به ASCII
ascii_encoded = auth_json.encode('ascii')

# تبدیل بایت‌های ASCII به base64
base64_encoded = base64.b64encode(ascii_encoded)

# دیکد کردن base64 به رشته
base64_string = base64_encoded.decode('ascii')

# چاپ نتیجه نهایی
print("Base64 Encoded String:")
print(base64_string)

# برای دیکد کردن از base64 به JSON
decoded_bytes = base64.b64decode(base64_string)
decoded_string = decoded_bytes.decode('ascii')
decoded_dict = json.loads(decoded_string)

# چاپ دیکشنری دیکد شده
print("Decoded JSON Dictionary:")
print(decoded_dict)
"""