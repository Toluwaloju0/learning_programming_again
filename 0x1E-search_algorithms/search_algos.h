#ifndef search_algos_h
#define search_algos_h

/* include all needed components */
#include <stdio.h>

/* define all used functions */
int linear_search(int *array, size_t size, int value);
int binary_search(int *array, size_t size, int value);
int jump_search(int *array, size_t size, int value);
int interpolation_search(int *array, size_t size, int value);
int exponential_search(int *array, size_t size, int value);


#endif