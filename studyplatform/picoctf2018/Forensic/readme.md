## PicoCTF2018 :  Forencisc  

---

#### Name :  forensics_Warmup1
- Desciption
    ```
    Can you unzip this file for me and retreive the flag?
    ```
- Walk Throught
  - 1.File Download
    ```
    https://2018shell.picoctf.com/static/d6487f8e2cbbb28b5168b512f0ac0710/flag.zip
    ```
  - 2.unzip
  - 3.open "flag.jpg"
---


#### Name : forensics_Warmup2
- Desciption
    ```
    Hmm for some reason I can't open this PNG? Any ideas?
    ```
- Walk Throught
  - 1.File Download
    ```
    https://2018shell.picoctf.com/static/0fde1a3e09824365348827194db9cdde/flag.png
    ```
  - 2.Open png
  - 3.Read Flag
---

#### Name : Desrouleaux
- Desciption
    ```
    Our network administrator is having some trouble handling the tickets for all of of our incidents. Can you help him out by answering all the questions? Connect with nc 2018shell.picoctf.com 54782. incidents.json
    ```
- Walk Throught
  - There is 3-Question
  ```
  1. What is the most common source IP address? If there is more than one IP address that is the most common, you may give any of the most common ones.

  2.How many unique destination IP addresses were targeted by the source IP address 231.205.245.44?

  3.What is the number of unique destination ips a file is sent, on average? Needs to be correct to 2 decimal places. 
  ```
  - Reference file : most_script.py

---

#### Name : Reading_Between_the_Eyes
- Desciption
    ```
    Stego-Saurus hid a message for you in this image, can you retreive it?
    ```
- Walk Throught
  - Steghide online decoder
    - https://stylesuxx.github.io/steganography/

---

#### Name : Recovering From the Snap
- Desciption
    ```
    There used to be a bunch of animals here, what did Dr. Xernon do to them?
    ```
- Walk Throught
  ```
  Think
    How to "dd" extension file Analysis?
  ```

  -  First Ways
     - foremost
  - Secnond ways
     - testdisk

---