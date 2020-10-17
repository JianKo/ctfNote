# HackToBer CTF

## About Site : https://www.ghosttown.xyz/t/week-is-50-complete/35

## Start
```
[Rules1]
- Read Manual 
- flag : flag{pl4y_by_th3_ru13s}

[DEADFACE]
- READ : http://ctf.cyberhacktics.com/intel 
- flag : flag{7}

[DEADFACE]
- READ : http://ctf.cyberhacktics.com/intel 
- flag : flag{mort1cia}

[Let's BEGIN]
- flag : flag{lets_get_started}
```

## LINUX
```
[SSH Credential]
ssh hacktober@env.hacktober.io
PASSWORD : hacktober-Underdog-Truth-Glimpse

[Talking to the dead]
flag1.txt ->  find / -name "flag1.txt" 2>dev/null
flag{cb07e9d6086d50ee11c0d968f1e5c4bf1c89418c}

flag2.txt -> find / -name "*flag*" 2>/dev/null
/home/luciafer/Documents/.flag2.txt
```

## Programming
```
[Message in an Array]
- USE THIS SITE : https://dotnetfiddle.net/
- flag : flag{Nothing Will Stop DEADFACE}

[Trick or Treat]
- unzip file
- function call it
- flag{2f3ba6b5fb8bb84c33b584f981c2d13d}

[Haunted Mirro]
- Reverse tool : ghidra 
- flag is showing
- flag : flag{XQwG1PhUqJ9A&5v}


```

## Cryptography
```
[Hail Caesar!]
- READ : https://www.dcode.fr/caesar-cipher
- Decode Message : TGG KUSJWV QGM
- amount : 1
- flag : flag{BOO SCARED YOU} 

[Down the Wrong Path]
-- Transposition Cipher
-- USE : https://www.dcode.fr/transposition-cipher
-- MESSAGE
RMTLOBBTERSUXT EBOLOOOHWGORTA METSKIUETEFNAC EREPYATNATOETK
--
- flag : flag{spookyboi}
```

## OSINT
```
[Creeping1]
- READ : https://www.facebook.com/ali.tevlin.5/about
- flag : flag{F. Kreuger Financial}

[Creeping2]
- READ : https://www.facebook.com/ali.tevlin.5/about
- flag : flag{Senior Acquisitions Supervisor}

[Creeping3]
- READ : https://www.facebook.com/ali.tevlin.5/about
- flag : flag{06 Jun 1973}


```

## SQL
```
[Past Demons]
1. file download 
2. mv *.unzip
3. sqlite3 out.db
4. .tables
5. select * from user;
6. select * from passwd;
: Password Crack : CrackStation
--> flag : 	flag{zxcvbnm}

[Address Book]
1. file search keyword "Havron"
--> flag: flag{luc1afer.h4vr0n@shallowgraveu.com}

[Body Count]
1. create database hacktober;
2. use hacktober;
3. sourcce *.sql 
4. select * from user;
--> flag : flag{900}

[NULL and Void]
--> flag : flag{middle, show}

[Fall classes]
Query : select count(distinct course_id) from term_courses where term_id=2;
--> flag : flag{401}

```


