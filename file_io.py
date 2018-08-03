#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" File input and output operations """

INPUT_FILE = "some_text.txt"
OUTPUT_FILE = "output.txt"
# NOFILE = "dioooos.txt"


with open(INPUT_FILE) as f:
    content = f.read()

print(content)

# with open(NOFILE) as nof:
#     content = nof.read()

# print(content)

with open(INPUT_FILE) as f:
    first_line = f.readline()
    second_line = f.readline()
    third_line = f.readline()

print("First line: ", first_line)
print("Second line: ", second_line)
print("Third line: ", third_line)

with open(OUTPUT_FILE, "w") as f:
    f.write(third_line)
    f.write(second_line)
    f.write(first_line)


with open(OUTPUT_FILE) as f:
    content2 = f.read()

print(content2)
