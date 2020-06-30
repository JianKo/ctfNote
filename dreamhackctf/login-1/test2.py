import jwt

jwt2 = jwt.encode({'id':'1'} , '',algorithm='none')

print(jwt2)
