#!/usr/bin/env python
import sys



#------------------------------------------------------------------------
        
#Reducer Code:
#Input is <show, viewer_count> and <show, channel>
#Input files 
#Returns viewer counts for tv shows that air on ABC.


#Generate Variables
#start by initializing previous shows to blank string
previous_show= " "   #start by initializing previous shows to blank string 
current_show= " " #initialize current show to blank string            
show_is_abc= 0 #variable shows if the show is on ABC
total_viewers= 0 #total viewers
line_count= 0  #count of input lines


for line in sys.stdin:
    line= line.strip() #strip out carriage return
    key_value= line.split('\t') #split lines, divide into key and value,then returns a list
    line_count= line_count+1     

    current_show= key_value[0] #1st item is key
    value_in= key_value[1] #2nd item is value


#Now need to check if it is a new show versus the 1st line 
#If it is, then print out the list of dates and counts

    if current_show!= previous_show:

        if line_count>1 and show_is_abc==1:
	    print('{0} {1}'.format(previous_show,total_viewers))

		show_is_abc = 0
    		total_viewers = 0

    previous_show = current_show  #Assign previous show for the next set of input lines


#Determine if current show is from file <show, viewer_count> or <show, channel>
#Then compute the total amount of viewers
    
    if value_in == 'ABC'or value_in.isdigit(): 
        
        show_is_abc = 1

    else:

        total_viewers += int(value_in)


#Print last join result
print('{0} {1}'.format(current_show,total_viewers))