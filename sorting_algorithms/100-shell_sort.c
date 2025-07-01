#include "sort.h"

/**
 * shell_sort - to sort an array using the shell sort method
 * @array: the array to be sorted
 * @size: the size of the array
 */


void shell_sort(int *array, size_t size)
{
	size_t gap = 1, ind;
	int temp;

	/* get the gap to be used using knuth sequence */
	while (gap < size / 3)
	{
	gap = (gap * 3) + 1;
	}
	/* implement the shell sort algorithm */
	for (; gap >= 1; gap /= 3)
	{
		for (ind = 0; ind < size; ind++)
		{
			if (gap + ind > size - 1)
				break;
			if (array[ind] > array[ind + gap])
			{
				temp = array[ind];
				array[ind] = array[ind + gap];
				array[ind + gap] = temp;
			}
		}
		print_array(array, size);
	}
}