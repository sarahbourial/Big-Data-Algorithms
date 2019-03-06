#!/usr/bin/env python
import sys

# The input file takes the form <matrix_name, row, column, value>;
# The mapper consists of a simple code:
# for matrix A we write the line first
# for matrix B we write the column first

for line in sys.stdin: 
    line =line.strip()
    source_matrix, row, col, value = line.split(',') 
    
    if source_matrix=='A':
        print ('{1}\t{0},{2},{3}'.format(source_matrix, row, col, value))
    else:
        print ('{2}\t{0},{1},{3}'.format(source_matrix, row, col, value))