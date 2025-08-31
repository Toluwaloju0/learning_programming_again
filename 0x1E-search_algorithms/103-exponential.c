#include "search_algos.h"

/**
 * exponential_search - a function to perform a search using exponential search algorithm
 * 
 * @array: the array to be searched
 * @size: the size of the array
 * @value: the value to be searched for
 * 
 * Return: the index of the value in the array else -1
 */

int exponential_search(int *array, size_t size, int value)
{
    size_t ind = 1, low = 1, high = 1, mid, iter;

    if (array == NULL || size == 0)
        return -1;
    if (array[0] == value)
        return 0;

    printf("Value checked array[%ld] = [%d]\n", ind, array[ind]);
    if (array[ind] == value) {
        printf("Value found between indexes [%ld] and [%ld]\n", ind, ind);
        printf("Searching in array: %d\n", array[ind]);
        return ind;
    }

    do {
        ind *= 2, low = ind / 2;  /* get the low point of the array for a binary search */
        if (ind > size - 1)
            ind = size - 1, size = 0;

        printf("Value checked array[%ld] = [%d]\n", ind, array[ind]);
        if (array[ind] >= value) {
            /** check if the value is within this range as the number at the array
              * index is greater than the value to be searched
              */
            high = ind, mid = (low + high) / 2;
            printf("Value found between indexes [%ld] and [%ld]\n", low, high);

            /* use a while loop for the binary search process */
            while (mid > 0) {
                printf("Searching in array: ");
                for (iter = low; iter <= high; iter++) {
                    if (iter == high)
                        printf("%d\n", array[iter]);
                    else
                        printf("%d, ", array[iter]);
                }
                mid = (low + high) / 2;
                if (array[mid] == value)
                    return mid;
                else if (array[mid] > value)
                    high = mid - 1;
                else
                    low = mid + 1;
            }
            return -1;
        }
    } while (ind < size || size > 0);
    return -1;
}