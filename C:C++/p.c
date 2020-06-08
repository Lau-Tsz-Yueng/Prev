#include <stdio.h>
#include <string.h>
#define SIZE 20

int main(int argc, char const *argv[])
  {
    char str1[SIZE] = "A\0A";
    char str2[SIZE] = "BBB";

    strcat(str1, str2);
    puts(str1);

    strncat(str1, str2, 2);
    puts(str1);

    return 0;
}
