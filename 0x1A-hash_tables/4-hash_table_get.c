#include "hash_tables.h"

/**
 * hash_table_get - to get the value stored in the hash table of the key
 *
 * @ht: the hash table
 * @key: the key storing the value
 */

char *hash_table_get(const hash_table_t *ht, const char *key)
{
	unsigned long int key_ind;

	if (ht == NULL)
		return NULL;

	key_ind = key_index((const unsigned char *)key, ht->size);

	while (ht->array[key_ind])
	{
		if (strcmp(ht->array[key_ind]->key, key) == 0)
			return (ht->array[key_ind]->value);
		ht->array[key_ind] = ht->array[key_ind]->next;
	}
	return NULL;
}