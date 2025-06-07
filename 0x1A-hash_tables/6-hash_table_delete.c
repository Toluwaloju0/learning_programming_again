#include "hash_tables.h"

/**
 * free_hash_node - to free a hash node
 * @hash_node: the hash node
 */

void free_hash_node(hash_node_t *hash_node)
{
	hash_node_t *temp;

	if (!hash_node)
		return;
	while (hash_node)
	{
		temp = hash_node->next;
		free(hash_node->key);
		free(hash_node->value);
		free(hash_node);
		hash_node = temp;
	}
}

/**
 * hash_table_delete - to completely delete a hash table and free it from memory
 *
 * @ht: the hash table
 */

void hash_table_delete(hash_table_t *ht)
{
	unsigned long int j;

	if (!ht)
		return;

	for (j = 0; j < ht->size; j++)
	{
		free_hash_node(ht->array[j]);
	}
	free(ht->array);
	free(ht);
}