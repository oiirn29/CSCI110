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

lines = mynewhandle.readlines()         #defines how to deal with the lines 

for line in reversed(lines):            #loop that grabs all the line in reverse
    
    print(line, end="")         #prints the lines

mynewhandle.close()         #closes the file 