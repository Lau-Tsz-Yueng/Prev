#include <stdio.h>
#define MAX_SIZE 8
const int TRUE = 1;
const int FALSE = 0;

int search_data(const int array[], const int size, const int target){

	int i = 0;

	for (i = 0; i < size; ++i){
		if (target == array[i])
			return 1;
	}

	return 0;
}

int main(void){
	int q[MAX_SIZE] = {7, 5, 0, 89, 12, 4, 31, 54};
	int x = 0;
	int i = 0;

	printf("Elements in the array:\n");
	for (i = 0; i < MAX_SIZE; ++i)
		printf("%4d", q[i]);

	printf("\nPlease input the target number:")
	scanf("%d", &x);

	if (TRUE == search_data(q, MAX_SIZE,x)){
		printf("%4d exists in this array.\n", x);
	}else{
		printf("Can not find %d in this array.\n", x);
	}

	return 0;
	


}