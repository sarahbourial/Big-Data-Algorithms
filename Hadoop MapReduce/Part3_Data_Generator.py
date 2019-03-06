#!/usr/bin/env python 
import sys
import random

# 1st argument: inputed by the user, it corresponds to the maximum value a number in the matrix can take
s = int(sys.argv[1]) 

# 2nd argument: number of rows for matrix A
m = int(sys.argv[2]) 

# 3rd argument: number of columns of A and number of rows of B

n = int(sys.argv[3]) 

# 4th argument: number of columns of B
p = int(sys.argv[4]) 

#This method should make sure no dimensionality issues arises

#Create A and B as empty lists
A=[] 
B=[]

# Now, randomly generate enough numbers for each matrix to match the specified dimensions
for i in range(0,m*n):
    A.append(random.randint(0, s))
for i in range(0,n*p):
    B.append(random.randint(0, s))
    
x=0    

for i in range(0,m): #these are the rows for A
    for j in range(0,n): #these are columns for A
        print ('A,{0},{1},{2}'.format(i+1,j+1,A[x]))
	#print ('{1} [A,{0},{2}]'.format(i+1,j+1,A[x]))
        x+=1
x=0 

for i in range(0,n):#these are the rows for B
    for j in range(0,p):#these are columns for B
        print ('B,{0},{1},{2}'.format(i+1,j+1,B[x]))
	#print ('{0}, [B,{1},{2}]'.format(i+1,j+1,B[x]))
        x+=1


