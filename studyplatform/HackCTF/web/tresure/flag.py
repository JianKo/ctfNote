import re
import requests

url = "http://ctf.j0n9hyun.xyz:2025/?page="


for x in range(1224,1500):

	r = requests.get(url+str(x))
	print(url+str(x))

	if re.findall("HackCTF{.*}",r.text):
		print(r.text)
		break

# key 1225
# flag is HackCTF{0hhhhh_5o_g0od_try!}