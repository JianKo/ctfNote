#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, char *argv[]) {

	char *ptr;
	
	ptr = getenv(argv[1]);
	
	printf("%p\n" ,ptr);

	return 0 ;
}
