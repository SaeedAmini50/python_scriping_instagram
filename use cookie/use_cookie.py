import json

# دیکشنری کوکی‌ها
cookies = {
    "mid": "ZldhhAALAAF-7gV6vCGU3KGP1nlo",
    "ig_did": "0C038DB6-B2BB-4CDD-970C-20C406BCCE39",
    "datr": "i2FXZprx2SPdIPHEuWn2mKQi",
    "dpr": "1.5",
    "ps_n": "1",
    "ps_l": "1",
    "ig_nrcb": "1",
    "csrftoken": "Df54ZRB9EM1QDDs7MJrK9YwkCdNsSln2",
    "ds_user_id": "66089215806",
    "ig_direct_region_hint": "NHA\\05466089215806\\0541750769501:01f7fa67961faf8339b32c3a98c243d764fffb30f094db9da34eaba49fb68f81bb1a56f6",
    "sessionid": "66089215806%3Ar7NgEpzILUTJuH%3A20%3AAYeYnQudUflOaByODhw2dv8C4DXqgXEi7mq-aQ8qWQ",
    "shbid": "16260\\05466089215806\\0541750953060:01f7c5038488dbb5d019d0149166d3f6801d54dd6f5c3e32e476c8f642b86bd022590674",
    "shbts": "1719417060\\05466089215806\\0541750953060:01f72d98fa0b209db8e8a70c3f3a7b441248d7b9436d9bd77e844711deaf36bb1e65786e",
    "wd": "1272x298",
    "rur": "NCG\\05466089215806\\0541750953627:01f72dc762f15f713092be34d346ceaa21e12ef1e71fef9835ff9494d64d2b5146bb02e8"
}

# ذخیره کوکی‌ها در فایل JSON
with open("inst_COOKIE.json", "w") as file:
    json.dump(cookies, file)

print("Cookies saved to inst_COOKIE.json")