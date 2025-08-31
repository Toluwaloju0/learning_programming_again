#include "search_algos.h"
#include <math.h>
/**
 * jump_search - a function to search an array using jump search algorithm
 * 
 * @array: the array to be searched
 * @size: the size of the array
 * @value: the value to be searched for
 * 
 * Return: the index of the value if present else -1
 */

int jump_search(int *array, size_t size, int value)
{
    size_t ind = 0, jump, iter;

    if (array == NULL || size == 0)
        return -1; 

    /* get the jump size for the array i would use sqrt(size) to get the sqrt */
    jump = sqrt(size);
    while (ind < size) {
        printf("Value checked array[%ld] = [%d]\n", ind, array[ind]);
        if (array[ind] >= value) {
            printf("Value found between indexes [%ld] and [%ld]\n", ind - jump, ind);
            for (iter = ind - jump; iter <= ind; iter++) {
                printf("Value checked array[%ld] = [%d]\n", iter, array[iter]);
                if (array[iter] == value)
                    return iter;
            }
            return -1;
        }
        ind += jump;
    }
     printf("Value found between indexes [%ld] and [%ld]\n", ind - jump, ind);
    for (iter = ind - jump; iter < size; iter++) {
        printf("Value checked array[%ld] = [%d]\n", iter, array[iter]);
        if (array[iter] == value)
            return iter;
    }
    return -1;
}