#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
	int var1=101;
	char buf[10];
	
	fgets(buf,120,stdin);

	printf("buf address :0x%x\n" , (int)buf);
	printf("value check var1 : %d\n" ,var1);

	if( var1 == 102) {
		printf("buf :%s\n",buf);
	}

	return 0;
}

