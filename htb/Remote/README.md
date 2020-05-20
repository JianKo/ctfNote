# Hack The Box
  &nbsp; Machine : Rope <br>
  &nbsp; Machine IP : 10.10.10.180 <br>

# Scanning File
  &nbsp; Reference file : Gathering/RemoteScanning.txt <br>

# Install mount tool
  &nbsp; 1.Install nfs tools command on Kali linux
    &nbsp; https://www.hiroom2.com/2017/08/01/kalilinux-2017-1-nfs-common-en/

  &nbsp; 2.RPC tool using it
    &nbsp;https://resources.infosecinstitute.com/exploiting-nfs-share/#gref


# Information Gathering (Enumerating)
1. nmap -sC -sV -oN RemoteScanning.txt 10.10.10.180 <br>
  : base scanning..<br>
  : appear interesting port on 2049 <br>

2. nmap -sV --script=nfs-showmount -oN remote.nfs 10.10.10.180 <br>
  : Searching for something NFS Directory <br>
   
3. mount "/site_backups" folder <br>
  : showmount -e 10.10.10.180 ( find to connect for directory )<br>
  : mount -t nfs 10.10.10.180:/site_backups /mnt ( mount nfs directory )<br>
 
4. find . -name "\*.sdf" (interesting file.. ?)<br>
  : Try to search for information file <br>
  : You can see the result in filename "Gathering/logging.txt" <br>
  : Hash Value is "b8be16afba8c314ad33d812f22a04991b90e2aaa : baconandcheese " <br>
  : Decrypt Site -> https://md5decrypt.net/en/Sha1/#answer <br>
  : Question. What is sdf file ? <br> 

5. cat \*.sdf |grep admin >> logging.txt <br>
  : logging in *.sdf to file save  <br>

# Gaining Access





## Reference Site
https://www.exploit-db.com/exploits/46153

1. Walk Throught
https://phantominfosec.wordpress.com/2020/03/31/htb-remote-walkthrough/

2. Walk Throught
https://blog.csdn.net/qq_32261191/article/details/105082982