#include <stdio.h>

int main() {
	char buf2[10];
	char buf[10];

	
	printf("It Can be Overflow: ");
	fgets(buf,40,stdin);
	
	if(strncmp(buf2,"go",2) == 0 )
	{
		printf("Good Skill\n");
		setreuid(0,0);
		system("/bin/sh");
	}
	
	return 0;
}

