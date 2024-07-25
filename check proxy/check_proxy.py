import threading
import queue
import requests


q = queue.Queue()
valid_proxies=[]

with open("list_of_proxy.txt","r") as f:
    proxies=f.read().split("/n")
    for p in proxies: 
        q.put(p)

def check_proxies():
    global q
    while not q.empty():
        proxy=q.empty()
        try:
            res = requests.get("https://www.instagram.com/",proxies={"http:":proxy,"https:":proxy})
        except:
            continue
        if res.status_code == 200:
            print(proxy)

for _ in range(10):
    threading.Thread(target=check_proxies).start()