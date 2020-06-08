
#include <stdio.h>
#include <time.h>
#include 
#include <stdlib.h>

#define U 1
#define D 2
#define L 3
#define R 4


typedef struct Snake{
	int x;
	int y;
	struct Snake *next;
}Snake;

int score = 0, add = 10;
int HighScore = 0;
int status, sleeptime = 200;
Snake * head, *food; 
Snake * q;
int endgamestatus = 0;
HANDLE hOut;


int main(int argc, char const *argv[])
{
	int c;
	const 
	return 0;
}