#include <stdio.h>

int main(void){
	int a = 1;
	int * p;
	printf("a = %d\n", a);
	printf("&a = %p\n", &a);

	printf("input the address of a:");
	scanf("%p", &p);

	printf("*p = %d\n", *p);
	printf("p = %p\n", p);

	return 0;
}