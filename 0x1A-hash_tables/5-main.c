#include "hash_tables.h"
/**
* main - check the code
*
* Return: Always EXIT_SUCCESS.
*/
int main(void)
{
	hash_table_t *ht;
	ht = hash_table_create(1024);
	hash_table_print(ht);
	hash_table_set(ht, "c", "fun");
	hash_table_set(ht, "python", "awesome");
	hash_table_set(ht, "Bob", "and Kris love asm");
	hash_table_set(ht, "N", "queens");
	hash_table_set(ht, "Asterix", "Obelix");
	hash_table_set(ht, "Betty", "Cool");
	hash_table_set(ht, "98", "Battery Street");
	hash_table_set(ht, "dram","first collide");
	hash_table_set(ht, "vivency", "second collide");
	hash_table_set(ht, "hetairas", "Another collide with mentioner");
	hash_table_set(ht, "mentioner", "Another collide with hetairas");
	hash_table_print(ht);
	return (EXIT_SUCCESS);
}