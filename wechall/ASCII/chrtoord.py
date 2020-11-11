list1 = [84, 104, 101, 32, 115, 111, 108, 117, 116, 105, 111, 110, 32, 105, 115, 58, 32, 103, 108, 99, 97, 105, 112, 110, 109, 110, 103, 114, 114]


solution = ""

for x in list1:
	print(chr(x))
	solution += str(chr(x))

print(solution)