#include "hash_tables.h"

/**
 * hash_djb2 - A function to convert a string to a hashed value
 *
 * @str: the string to be converted
 * Return: the hashed string in interger form
 */

unsigned long int hash_djb2(const unsigned char *str)
{
	unsigned long int hash;
	int c;
	hash = 5381;
	while ((c = *str++))
	{
		hash = ((hash << 5) + hash) + c; /* hash * 33 + c */
	}
	return (hash);
}
