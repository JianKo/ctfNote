/* change return address */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

char buffer[32];

int main(int argc, char *argv[]) {
	char local[32];
	
	printf("buffer : 0x%x\n" ,&buffer);
	fgets(local,128 ,stdin);

	strcpy(buffer,local);

	return 0;
}
