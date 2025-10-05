#!/usr/bin/env python3
""" a module to create the pascal triangle """

def pascal_triangle(n):
    """to create a pascal triangle with length 'n'"""

    if n < 1:
        return []
    
    p_triangle = []
    for a in range(n):
        p_triangle.append([])
        for b in range(a + 1):
            if b == 0 or b == a:
                p_triangle[a].append(1)
                continue
            p_triangle[a].append(p_triangle[a - 1][b - 1] + p_triangle[a - 1][b])
        
    return p_triangle