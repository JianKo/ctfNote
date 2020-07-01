# Cheet Sheet

***ERROR***
```
#bits/libc-header-start.h: No such file or director
: sudo apt-get install gcc-multilib g++-multilib
```

***SYSTEM***
```
- 32bit Compile Option in Ubuntu (and BOF Option)
: gcc -m32 {} -fno-stack-protector example example.c 
```

***Disassemble Command***
```
objdump -d -M intel {File}
```
