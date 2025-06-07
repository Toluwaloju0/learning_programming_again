#include "hash_tables.h"

/**
 * hash_table_set - A function to set the hash table value given a specific key
 *
 * @ht: the hash table to be used
 * @key: the key used to store the hash table value
 * @value: the value to be stored in the hash table
 * Return: 1 on sucess and 0 on failure
 */

int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
	unsigned long int hash_index;
	hash_node_t *temp;

	if (ht == NULL || strcmp(key, "") == 0)
		return 0;
	hash_index = key_index((const unsigned char *)key, ht->size); /* the index to store the hash value */

	if (!ht->array[hash_index])
	{
		ht->array[hash_index] = malloc(sizeof(hash_node_t));
		if (!ht->array[hash_index])
			return (0);
		ht->array[hash_index]->key = strdup(key);
		ht->array[hash_index]->value = strdup(value);
		return (1);
	}
	temp = ht->array[hash_index];
	while (temp)
	{
		if (strcmp(key, temp->key) == 0)
		{
			free(temp->value);
			temp->value = strdup(value);
			return (1);
		}
		temp = temp->next;
	}
	temp = malloc(sizeof(hash_node_t));
	if (!temp)
		return (0);
	temp->key = strdup(key);
	temp->value = strdup(value);
	temp->next = ht->array[hash_index];
	ht->array[hash_index] = temp;
	return 1;
}