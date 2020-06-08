/*
 * bigint.h
 */

#ifndef BIGINT_H
#define BIGINT_H

#include <stdio.h>

/* Max 255 */
#ifndef BIGINT_MAX_DIGITS
#define BIGINT_MAX_DIGITS 255
#endif

/* Set this before #including for debug output */
#ifndef BIGINT_DEBUG
#define BIGINT_DEBUG 0
#endif

/*
 * bigint struct members
 *
 * s. Sign bit - can be 0 (positive) or 1 (negative)
 * d. The digits as unsigned char (literal byte value not ASCII)
 * n. The number of digits actually used for this int
 */
struct _bigint {
    unsigned char s;
    unsigned char d[BIGINT_MAX_DIGITS];
    unsigned char n;
} typedef bigint;

/* Write ASCII decimal representation of bigint to output stream ofile. */
void bigint_print_d(bigint bi, FILE* ofile);

/* Get a bigint from a decimal string representation */
bigint bigint_from_string_d(const char* str);

/* Negate a bigint */
bigint bigint_neg(bigint bi);

/* Less than: bi1 < bi2 */
int bigint_lt(bigint bi1, bigint bi2);

/* Equal to: bi1 == bi2 */
int bigint_eq(bigint bi1, bigint bi2);

/* Less or equal: bi1 <= bi2 */
int bigint_le(bigint bi1, bigint bi2);

/* Add two bigints */
bigint bigint_add(bigint bi1, bigint bi2);

/* Subtract two bigints */
bigint bigint_sub(bigint bi1, bigint bi2);

/* Multiply bigint by a bigint */
bigint bigint_mul(bigint bi1, bigint bi2);

/* Divide bigint by bigint */
bigint bigint_div(bigint bin, bigint bid);

#endif // BIGINT_H
