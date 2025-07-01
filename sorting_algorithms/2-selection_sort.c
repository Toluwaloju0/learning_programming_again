#include "sort.h"

/**
 * selection_sort - to sort an array using selection sort method
 * @array: the array to be sorted
 * @size: the size of the array
 */

void selection_sort(int *array, size_t size)
{
	size_t index, next_index, temp;

	for (index = 0; index < size - 1; index++)
	{
		for (next_index = index + 1; next_index < size; next_index++)
		{
			if (array[next_index] < array[index])
			{
				temp = array[index];
				array[index] = array[next_index];
				array[next_index] = temp;
				print_array(array, size);
			}
		}
	}
}