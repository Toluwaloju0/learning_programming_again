#include "search_algos.h"
#include <stdio.h>
/**
 * linear_search - a function to search an array using linear search method
 * 
 * @array: the array to be searched
 * @size the size of the array
 * @value: the value to be searched for
 */

int linear_search(int *array, size_t size, int value)
{
    size_t ind;

    if (array == NULL)
        return -1;

    /* iterate through the array and check the values */
    for (ind = 0; ind < size; ind++) {
        printf("Value checked array[%ld] = [%d]\n", ind, array[ind]);
        if (array[ind] == value)
            return ind;
    }
    return -1;
}