import flag, shift

list_ = ['0x475', '0x3b0', '0x471', '0x47a', '0x39c', '0x465', '0x476', '0x46d', '0x46d', '0x47a','0x39c', '0x460', '0x471', '0x47a', '0x473', '0x477', '0x3b3', '0x3a2', '0x3a2']

# def encrypt(d,shift):
# 	e = []
# 	for c in d:
# 		e.append(hex((ord(c)+shift)^99))
# 	return e
#
# if list(encrypt(flag,shift)) == list_:
# 	print("encoding success!!")

for i in range(951):
    e = []
    for c in list_:
        try:
            e.append(chr((int(c,16)^99 )-i))
        except:
            pass
    str_ = ''.join(e)
    print(str_)