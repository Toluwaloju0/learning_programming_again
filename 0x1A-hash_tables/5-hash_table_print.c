#include "hash_tables.h"

/**
 * hash_table_print - to print a hash table
 *
 * @ht: the hash table
 */

void hash_table_print(const hash_table_t *ht)
{
	unsigned long int j, k = 0;
	hash_node_t *temp;

	if (ht == NULL)
	{
		printf("{}");
		return;
	}
	
	printf("{");
	for (j = 0; j < ht->size; j++)
	{
		temp = ht->array[j];
		while (temp)
		{
			if (k > 0)
				printf(", ");
			printf("\'%s\': \'%s\'", temp->key, temp->value);
			k++;
			temp = temp->next;
		}
	}
	printf("}\n");
}