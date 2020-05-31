#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	long sh = 0xf7e1dd10;
	while(memcmp((void *)sh, "/bin/sh", 8)) sh++;
	printf("/bin/sh => 0x%08x\n" ,sh);
	return 0;
}
