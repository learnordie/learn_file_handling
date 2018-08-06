#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Read a comma separated file into a list """

import csv

M_COMMAS = "multiple_lines_commas.txt"


# Everything in a single list
with open(M_COMMAS) as f:
    single_list = []
    reader = csv.reader(f)
    for row in reader:
        for e in row:
            single_list.append(e)


# Every line of the line in a list
with open(M_COMMAS) as f:
    separated_lists = []
    reader = csv.reader(f)
    for row in reader:
        separated_lists.append(row)


print(single_list)
print(separated_lists)
