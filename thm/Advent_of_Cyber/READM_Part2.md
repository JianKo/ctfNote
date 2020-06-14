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