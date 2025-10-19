#!/usr/bin/python3

""" a module to define a function which checks the number of operations that can be carried out when copying a file"""

def minOperations(n):
    """ a function to count the minimum number of times a string can be replicated n times"""

    count, num = 0, 0

    # copy_all occurs when "(num + 1) < (n: remaining characters to be copied / 2)"  
    while n > 0:
        print("first iteration")
        n -= num
        if num + 1 < n / 2:
            num += 1
            count += 1
        if num > n and n != 0:
            return 0
        count += 1
        print("========================", n, "=======================================")
    
    return count
