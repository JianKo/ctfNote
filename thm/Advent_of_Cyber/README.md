asdasd# MACHINE : Advent of Cyber


***Day 1***
```
Elf (cookie modifyed attack)
Inventory Managemnt
#1 What is the name of the cookie used for authentication?
:authid

#2 If you decode the cookie, what is the value if the fixed part of the cookie
:v4er9ll1!ss

#3 After accessing his account, what did the user mcinventory request?
: firewall

```

***Day 2***
```
Arctic Forum (OSINT)
#1 What is the path of the hidden page?
: gobuster dir -u {IP} -w{Dictionary}
: /sysadmin

#2 What is the password you found?
: it is OSINT!
: find github repo
: defaultpass

#3 What do you have to take to the "partay"
: read the access page!

```

***Day 3***
```
Evil Elf ( *.pcap analysis)
#1 Whats the destinatnion IP on packet number 998
:63.32.89.195

#2 What item is on the christmas list?
: ps4

#3 Crack buddy's password:
:rainbow 

SHORT NOTE
: #1 click the right button -> scroll down
: #2 statistics ->  EndPoints -> fist list right click -> find
: #3 sha512 dictionary cracking with haschcat command
   hashcat -a 0 -m 1800 hash {password_list_path} --force

```

***Day 4***
```
Trainig
#1 how many visible files are there in the home directory(excluding ./ and ../)?
: 8

#2 What item is the content of files5?
: recipes

#3 which file contains the string password?
: file6 

#4 whay is the IP address in a file in the home folder?
:  10.0.0.05
: Refer linke : https://www.putorius.net/grep-an-ip-address-from-a-file.html

#5 How may users can log into the machine?
: log means login
: cat /etc/passwd | grep /bin/bash
: 3

#6 What is the sha1 hash of file8?
: sha1sum file8

#7 Finding the has?
: find / -name "*shadow*" -exec ls lt {} \; 2>/dev/null 
or
: find / -name "*shadow*" 2>/dev/nul/

```


