#include "hash_tables.h"

/**
 * key_index - to get the index of the given key
 *
 * @key: the key of used to store the hash table value
 * @size: the size of the hash table
 */

unsigned long int key_index(const unsigned char *key, unsigned long int size)
{
	return(hash_djb2(key) % size);
}
