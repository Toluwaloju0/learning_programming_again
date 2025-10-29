#!/usr/bin/env python3

from sys import argv, stderr

if len(argv) < 2:
    print("Usage: ./markdown2html.py README.md README.html")
    exit()
try:
    unordered, ordered = [], []
    with open(argv[1], 'r') as file:
        for line in file:
            line = line.split(' ', 1)
            if line[0][0] == "#":
                print(f"<h{len(line[0])}>{line[1][0 : -1]}</h{len(line[0])}>")
            elif line[0][0] == "-":
                unordered.append(line[1][0:-1])
            elif line[0][0] == "*":
                ordered.append(line[1][0:-1])
        if len(unordered) > 0:
            print("<ul>")
            for item in unordered:
                print(f"\t<li>{item}</li>")
            print("</ul>")
        if len(ordered) > 0:
            print("<ol>")
            for item in ordered:
                print(f"\t<li>{item}</li>")
            print("</ol>")
except FileNotFoundError as e:
    print(f"Missing {argv[1]}", file=stderr)
    exit(1)