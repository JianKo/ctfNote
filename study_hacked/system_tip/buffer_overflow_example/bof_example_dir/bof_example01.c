#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
	char str[256];

	setreuid(0,0);
	strcpy(str,argv[1]);
	printf(str);
}
