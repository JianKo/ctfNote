/* change return address */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
	char local[32];
	
//	printf("buffer : 0x%x\n" ,&buffer);
	setreuid(0,0);
	//fgets(local,128 ,argv[1]);

	printf("local buffer :0x%x\n" ,(int)local);
//	printf("%s\n" ,local);
	strcpy(local,argv[1]);
	printf("%s\n" ,local);
	return 0;
}
