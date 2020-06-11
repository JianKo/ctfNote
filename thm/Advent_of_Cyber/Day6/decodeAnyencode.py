import base64
import codecs

def decodeToBase64(msg):
	b = msg.encode("utf-8")
	e = base64.b64encode(b)
	print("[+] Base64 Decode : " , msg)

def decodeToHex(msg):
	msg = bytes.fromhex(msg).decode("utf-8")
	print("[+] Hex Decode : ", msg)

msg = str(input("[+] INPUT the Any Text : "))


print("=========== BASE Number Decode ================")
decodeToBase64(msg)
print("\n")
print("=========== Hex Value Decode   ================")

decodeToHex(msg)