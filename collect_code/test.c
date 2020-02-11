#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	long i = 0x1234567;
	char buf[1024];

	if(argc > 1)
	strcpy(buf,argv[1]);

	printf("%s\n" ,buf);
	printf("%lx\n" ,i);

	if(i!= 0x1234567) {
		printf("sdsd");
	}
}
