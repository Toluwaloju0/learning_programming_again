#include <stdio.h>
#include <stdlib.h>
#include "sort.h"
/**
* main - Entry point
*
* Return: Always 0
*/
int main(void)
{
	int array[] = {19, 48, 99, 71, 1, 13, 52, 96, 73, 86, 7, 1};
	size_t n = sizeof(array) / sizeof(array[0]);
	print_array(array, n);
	printf("\n");
	selection_sort(array, n);
	printf("\n");
	print_array(array, n);
	return (0);
}
