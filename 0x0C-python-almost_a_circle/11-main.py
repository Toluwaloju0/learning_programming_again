#!/usr/bin/python3
""" 11-main """

from models.square import Square

if __name__ == "__main__":
    s1 = Square(5)
    print(s1)
    print(f"Area is {s1.area()}")
    s1.update(10)
    print(s1)
    print(f"Area is {s1.area()}")
    s1.update(1, 2)
    print(s1)
    print(f"Area is {s1.area()}")
    s1.update(9, 2, 3)
    print(s1)
    print(f"Area is {s1.area()}")
    s1.update(1, 2, 3, 4)
    print(s1)
    print(f"Area is {s1.area()}")
    s1.update(x=12)
    print(s1)
    print(f"Area is {s1.area()}")
    s1.update(size=9, y=1)
    print(s1)
    print(f"Area is {s1.area()}")
    s1.update(size=7, id=89, y=1)
    print(s1)
    print(f"Area is {s1.area()}")
