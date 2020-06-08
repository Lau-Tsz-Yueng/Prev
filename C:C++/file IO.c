#include <stdio.h>
#include <math.h>
#include <time.h>
#include <string.h>
#define SIZE 4oooo

struct Vector3D{
	int x;
	int y;
	int z;
}typedef Vec3D;

	int norm2(Vec3D vector);

	int main(int argc, char *argv[])
	{
		Vec3D some_vector = {3 ,4, 1};
		printf("some_vector has norm %d\n", norm2(some_vector));
		return 0;
}

int norm2(Vec3D vector)
{

	return vector.x * vector.x
	+ vector.y * vector.y
	+ vector.z * vector.z;

}

/* pstruct.c */

#include <stdio.h>

struct Vector3D
{
  int x;
  int y;
  int z;
} typedef Vec3D;

int main(int argc, char *argv[])
{
  Vec3D vec = {3, 4, 1};

  Vec3D *pvec = &vec;

  // These two are equivalent
  printf("(*pvec).x = %d\n", (*pvec).x);
  printf("pvec->x   = %d\n", pvec->x);

  return 0;
}


/* chario.c */

#include <stdio.h>

int main(int argc, char *argv[])
{
  /*
   * Open both files checking for success.
   */
  char infilename[] = "foo.txt";
  char outfilename[] = "bar.txt";

  FILE* infile = fopen(infilename, "r"); // read
  if(infile == NULL)
  {
    fprintf(stderr, "Unable to open \"%s\"\n", infilename);
    return 1;
  }

  FILE* outfile = fopen(outfilename, "w"); // write
  if(outfile == NULL)
  {
    fprintf(stderr, "Unable to open \"%s\"\n", outfilename);
    fclose(infile);
    return 1;
  }

  /*
   * read each character of infile and write to outfile
   */
  char character;
  for(;;) // <-- infinite loop
  {
    /*
     * Read character and check for End Of File
     */
    character = fgetc(infile);
    if(character == EOF)
    {
      break; // exit loop
    }

    /* convert to lower case */
    if('a' <= character && character <= 'z')
    {
      character -= 'a' - 'A';
    }

    /* Write to hte output file */
    fputc(character, outfile);
  }

  fclose(infile);
  fclose(outfile);
  return 0;
}


read chunks by chunks