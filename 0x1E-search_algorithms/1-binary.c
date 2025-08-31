#include "search_algos.h"

/**
 * binary_search - a function to search an array using binary search
 * 
 * @array: pointer to the first item of the array
 * @size: the size of the array
 * @value: the value to be searched
 * 
 * Return: the index of the value if present else -1
 */


int binary_search(int *array, size_t size, int value)
{
    size_t ind = 0, low = 0, high = size - 1, iter;

    if (array == NULL || size == 0)
        return -1;
    while (size > 0) {
        ind = (low + high) / 2;
        for (iter = low; iter <= high; iter++) {
            if (iter == high)
                printf("%d\n", array[iter]);
            else
                printf("%d, ", array[iter]);
        }
        if (array[ind] == value)
            return ind;
        else if (array[ind] > value)
            high = ind - 1;
        else
            low = ind + 1;
        size = size / 2;
    }
   return -1;
}