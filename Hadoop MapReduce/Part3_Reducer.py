#!/usr/bin/env python
import sys


#%%The reducer takes inputs of the form <number, matrix, number, value>
#Firt create dictionaries that will hold the necessary information

from collections import defaultdict

A = defaultdict(list) 
B = defaultdict(list)


#%%For line in list 
#k indicates the row in A and the column in B
#We Append dictionnary that will register row as key 
#And tuple (column, value) as value, for both A and B

for line in sys.stdin: 
    line = line.strip()	
    k, value = line.split('\t') 
    sourceMatrix, row_col, value = value.split(',')
    row_col = row_col.strip()
    if sourceMatrix == "A":
        A[int(k)].append((int(row_col), int(value))) 
    else:
        B[int(k)].append((int(row_col), int(value)))  
        
print(A)
print(B)
print(A[1])
print(A[1][0][1])
print(B[1][0][1])

#%% This loop will browse the keys in A; 
#So for each line in A and for each column in B, 
#We initialize value as 0, then i goes from 0 to the number of columns of A -1
#We perform the multiplication of A(i,j) by B(j,i) and we add the values obtained

for k in A: 
	for j in B: 
		value=0 
		for i in range(len(A[1])): 
			Add = int(A[k][i][1]) * int(B[j][i][1])  
			value+=Add
		key='[%s, %s]' % (k, j)
		print '%s\t%s' % (key, value) 
		
	
	




