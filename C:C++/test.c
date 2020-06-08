#include <stdio.h>
#include <math.h>

int main(void)
{
	int a ,b, c;
	int judge = 0;
	printf("please input 3 lengths of a triangle:");
	scanf("%d, %d, %d", &a, &b, &c);
	float area = (0.5*a*b*sin(c));
	switch(judge)
	{
		case 1:
	   		if ((a + b > c) == 0){printf("this is not a triangle!"); return 1;}
	   		break;
		case 2:
			if ((c + b > a) == 0){printf("this is not a triangle!"); return 1;}
			break;
		case 3:
			if ((a + c > b) == 0){printf("this is not a triangle!"); return 1;}
			break;
        case 4:
        	printf("this is a triangle!");
	}
	printf("And its area is equal to %f!\n", area);
	return 0;
}