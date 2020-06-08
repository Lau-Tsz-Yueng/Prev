/*command line programs

std streams: stdin, stdout, stderr

$ for x in *.c; gcc do -std=c99 -Wall $x -o $x.exe; done

the command line interface

Input:  arguments via argc and argv
		text/data on stdin
		environment variables
Output: text/data n stdout, stderr
		return codes(Success or Failure)

argc argv
int argc
argv is *char[]
it means an array of strings
*/


/*
#include <stdio.h>

int main(int argc, char *argv[])
{
	for(int i = 0; i <argc; i++)
	{
		puts(argv[i]);
	}
	return 0;
}
*/
/*
reading from stdin

stdin = standard Input
*/
/*
#include <stdio.h>

int main(int argc, char *argv[])
{
	printf("Please enter a character:");
	int c = fgetc(stdin);
	if (c == EOF)
	{
		fprintf(stderr, "\nSomething went wrong..\n");
		return 1;
	}
	printf("You enter '%c\n", (char)c);

	return 0;
}
*//*
stdout = standard Output
stderr = standard error

We use stdout for normal output when the program is working fine.
We use stderr to print error messages when something goes wrong.
*/
#include <stdio.h>

int main(int argc, char *argv[])
{
	printf("This is a message to stdout\n");
	fprintf(stdout, "So is this...\n");
	fprintf(stderr, "This is one is for stderr\n");
	return 0;
}
The 3rd line of main shows that we can also print to stderr instead of stdout
(there is no conveience function for stderr).

$ cat xxx.txt


There are many reasons for distinguishing between stdout asnd stderr. Here are a few:

If stdout is redirected to a file then the user will probably still want to see error messages.
The output on stdout might be enourmous in which case it might be hard to spot one line in the middle that shows an important error message.
The output on stderr might just be an ignorable warning about a possible problem when the output from stdout might be going to a file that we want to use for some other purpose - mixing in the error messages with the other data may corrupt the file.
For simple programs the output rules are simple: all output goes to stdout unless something goes wrong. When something goes wrong the program should print a single (ideally informative) error message on stderr and immediately abort.

The command echo $? prints the return code of the previously run program. 






