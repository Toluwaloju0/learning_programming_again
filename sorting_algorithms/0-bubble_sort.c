#include "sort.h"

/**
 * get_largest - A function to get the index of the largest value of an array
 *
 * @array: the array to be checked
 * @size: The size of the array
 * Return: the index of the largest value
 */

int get_largest(int *array, int size)
{
	int a, largest_index = 0;

	for (a = 1; a < size; a++)
	{
		if (array[a] >= array[largest_index])
			largest_index = a;
	}
	return largest_index;
}


/**
 * bubble_sort - the bubble sort algorithm function
 * 
 * @array: the array to be sorted 
 * @size: the size of the array
 */

void bubble_sort(int *array, size_t size)
{
	int temp, a, b = size;

	while (b > 0)
	{
		for (a = get_largest(array, b); a < b - 1; a++)
		{
			temp = array[a + 1];
			array[a + 1] = array[a];
			array[a] = temp;
			print_array(array, size);
		}
		b--;
	}
}