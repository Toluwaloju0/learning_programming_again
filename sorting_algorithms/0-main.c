#include "sort.h"
#include <stdio.h>

/**
* main - Entry point
*
* Return: Always 0
*/
int main(void)
{
	int array[] = {0, 19, 48, 99, 71, 13, 52, 96, 73, 86, 9};
	size_t n = sizeof(array) / sizeof(array[0]);
	print_array(array, n);
	printf("\n");
	bubble_sort(array, n);
	printf("\n");
	print_array(array, n);
	return (0);
}
