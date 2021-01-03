local_17 = '683a3a44714c5e497839625d5539' 
local_17 = '443a3a68495e4c715d6239783955' # Little-Endian

local_9 = 0;
local_8 = 0;

tmp = ""
string = len(bytes.fromhex(local_17).decode('utf-8'))

for i in range(0,len(local_17)):
	if i % 2 == 0:
		pass
	else:
		
		pXor = int(local_17[i-1:i+1],16) ^10
		tmp += chr(pXor)
	local_8 = local_8 +1

print(tmp)
	