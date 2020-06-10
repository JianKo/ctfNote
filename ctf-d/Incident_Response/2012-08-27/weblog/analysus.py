from collections import Counter
from pprint import pprint

with open("./statusWord.log", "r") as read:
	total_word = [x for x in read]

	status = Counter(total_word)

	pprint(status)