#!/usr/bin/env python
import sys


#------------------------------------------------------------------------

#Mapper code 
#For input <show, view_count> and <show, channel>: input files, 
#For input <show, channel>,  include those where ABC is the channel only.


for line in sys.stdin:
    line       = line.strip()   
    key_value  = line.split(",")   #divide line between key and value,
    key_in     = key_value[0]   #1st list item: key
    value_in   = key_value[1]   #2nd list item: value 

#If this entry is 'ABC' or is a digit   
    if value_in == "ABC" or value_in.isdigit():           
    	print( '%s\t%s' % (key_in, value_in) ) 
