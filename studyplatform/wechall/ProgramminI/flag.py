# -*- coding:utf-8 -*-

import requests

url = "https://www.wechall.net/challenge/training/programming1/index.php?action=request"

dest = "https://www.wechall.net/challenge/training/programming1/index.php?answer="
cookie ={"Cookie" :"WC=12976522-56341-Ru8BwV8yzncfUzVa"}

r = requests.get(url,headers=cookie).text
response = requests.get(dest+r , headers=cookie).text

print(response)