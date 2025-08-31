#include "search_algos.h"

/**
 * interpolation_search - a function to search an array using interpolation algorithm
 * 
 * @array: the array to be searched
 * @size: the size of the array
 * @value: the value to be searched for
 * 
 * Return: the ind of the value in the array else -1
 */


int interpolation_search(int *array, size_t size, int value)
{
    size_t ind = 0, low = 0, high = size - 1;

    if (array == NULL || size == 0)
        return -1;
    
    while (size > 0) {
        ind = low + (((double)(high - low) / (array[high] - array[low])) * (value - array[low]));
        if (ind > size - 1) {
            printf("Value checked array[%ld] is out of range\n", ind);
            return -1;
        }
        printf("Value checked array[%ld] = [%d]\n", ind, array[ind]);
        if (array[ind] == value)
            return ind;
        else if (array[ind] > value)
            high = ind - 1;
        else
            low = ind + 1;
        size -= ind;
    }
    return -1;
}