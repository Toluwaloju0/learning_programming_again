#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "hash_tables.h"
/**
* main - check the code
*
* Return: Always EXIT_SUCCESS.
*/
int main(void)
{
	hash_table_t *ht;
	char *key = "synaphea";
	unsigned long int key_ind;
	int sucess;

	ht = hash_table_create(1024);
	sucess = hash_table_set(ht, key, "cool");
	if (sucess == 0)
		printf("failed");
	key_ind = key_index((const unsigned char *)key, 1024);
	while (ht->array[key_ind] != NULL)
	{
		printf("KEY: %s ------ VALUE: %s\n", ht->array[key_ind]->key, ht->array[key_ind]->value);
		ht->array[key_ind] = ht->array[key_ind]->next;
	}
	return (EXIT_SUCCESS);
}
