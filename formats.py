#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Read files with different formats and save the content on a list """

LINES = "different_lines.txt"
SPACES = "same_line_spaces.txt"
COMMAS = "same_line_commas.txt"
M_SPACES = "multiple_lines_spaces.txt"


# Read a file with several lines and store its content in a list
with open(LINES) as f:
    lines_list = [line.rstrip('\n') for line in f]


# Read a one line file with elements separated by spaces
# and store its content in a list
with open(SPACES) as f:
    # spaces_list = f.readline().split()
    spaces_list = f.read().split()


# Read a (one or) multiple lines file with elements separated by spaces
# and store its content in a list
with open(M_SPACES) as f:
    m_spaces_list = f.read().split()


# Read a one line file with elements separated by commas
# and store its content in a list
with open(COMMAS) as f:
    # commas_list = f.readline().split()
    commas_list = f.read().rstrip('\n').split(',')

print(lines_list)
print(spaces_list)
print(m_spaces_list)
print(commas_list)
