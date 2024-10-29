#-------------------------------------------------------------------------------
# Name:        13.11 exercise 1
# Purpose:   re-orders the lines in the .txt file provided by filepath
#
# Author: Joshua Mazurak
#
# Created:10/27/2024
# Licence: CC BY
#-------------------------------------------------------------------------------

file = input("file path: ")         #askes for yor text file

mynewhandle = open(file, "r")           #opens the file

file_output = open("file output.txt", "w")          #opens new file for the output 

lines = mynewhandle.readlines()         #defines how to deal with the lines 

for line in reversed(lines):            #loop that grabs all the line in reverse
    
    file_output.write(line)         #wites the reversed lines into a file 

mynewhandle.close()         #closes the file 
file_output.close()         #closes the file 
