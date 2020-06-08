#include <stdio.h>

int main(void)
	{
	
	int a = 0;

	printf("Enter switch structure 1:\n");

	printf("Select a branch:");

	scanf("%d", &a);
	
	switch(a)
	{
		case 1:
			printf("\tbranch 1\n");
		case 2:
			printf("\tbranch 2\n");
		case 3:
			printf("\tbranch 3\n");
		default:
			printf("\twrong case\n");
	}

	printf("Enter switch structure 2:\n");
	printf("Select a branch:");
	scanf("%d", &a);

	switch(a){
		case 1:
			printf("\tbranch 1\n");
			break;
		case 2:
			printf("\tbranch 2\n");
			break;
		case 3:
			printf("\tbranch 3\n");
			break;
		default:
			printf("\twrong case\n");
			break;
	}

	return 0;
}