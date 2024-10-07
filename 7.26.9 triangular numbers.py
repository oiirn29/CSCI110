#-------------------------------------------------------------------------------
# Name:        7.26 exercise 9
# Purpose:   create a function that calculates triangular 
#            numbers which is the amout of "dots" 
#            that it'll take to make an equalaral trangle 
#
# Author:Joshua Mazurak
#
# Created:10/6/2024
# Licence: CC BY
#-------------------------------------------------------------------------------

def print_triangular_numbers(n):        #creates a function that contains the math protion of the exercise

    for r in range(1, n+1):     #creates a for loop that continues the math 

        dots = r * (r + 1) // 2     #the triangular number represents the total dots that can form an equilateral triangle with r rows

        print (f"{r}\t{dots}")      #prints output

print_triangular_numbers(5)     #calls function