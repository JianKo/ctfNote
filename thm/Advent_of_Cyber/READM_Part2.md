# MACHINE : Advent of Cyber

***Day 12***
```
Elf Applications
#1 What is the md5 hashsum of the encrypted note1 file?
: md5sum {file}


#2 Where was elf Bod told to meet Alice?
: Santa's Grotto
: # method
: gpg -d {file}

#3 Decrypt note2 and obtain the flag!
:# method
: openssl rsautl -decrypt -inkey priavet.ket -in {file_encrypt} -out {save_decrypt_file}
```

***Day 13***
```
Accumlate
#1 A web Server is running on the target. what is the hidden directory which the
website lives on?
: retro

#2 Gain initial access and read the contents fo user.txt
: remmina rdp cliet use it

#3 [Optional] Elevate privileges and read the content of root.txt
:hhupd.exe Privilege Escalte
```

***Day 14***
```
Unknown Storage
Accumlate
#1 What is the name of the file you found?
:employee_name.txt

#2 What is in the file?
:mcchef

```

***Day 15***
```
LFI
#1 What is Charlie going to book a holiday to?
: Hawaii

#2 Read /etc/shadow and crack Charilies Password.
: password1
: method
: hashcat,vulner_function

#3 What is flag1.txt?
: read the flag
```