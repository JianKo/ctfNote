# Hack The Box
# Machine : Rope
# Machine IP : 10.10.10.180


## Reference Nmap Scanning : RemoteScanning.txt 

## Install mount tool
1. install nfs tools command on Kali linux <br>
https://www.hiroom2.com/2017/08/01/kalilinux-2017-1-nfs-common-en/<br>

2. rpc tool using it <br>
https://resources.infosecinstitute.com/exploiting-nfs-share/#gref<br>


# Information Gathering

[=] RemoteScanning.txt <br>
1. nmap -sC -sV -oN RemoteScanning.txt 10.10.10.180 <br>
  : base scanning..<br>
  : appear interesting port on 2049 <br>

[=] remote.nfs <br>
2. nmap -sV --script=nfs-showmount -oN remote.nfs 10.10.10.180 <br>
  : Searching for something Directory (bound NFS) <br>


3. mount "/site_backups" folder
  : showmount -e 10.10.10.180 -> find to connect for directory
  : mount -t nfs 10.10.10.180:/site_backups /mnt
  : Try to search for interesting information -> find . -name "\*.sdf"
  : Question. What is sdf file ?



## Reference Site

https://www.exploit-db.com/exploits/46153

1. Walk Throught
https://phantominfosec.wordpress.com/2020/03/31/htb-remote-walkthrough/

2. Walk Throught
https://blog.csdn.net/qq_32261191/article/details/105082982