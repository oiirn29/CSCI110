#-------------------------------------------------------------------------------
# Name:        5.14 exercise 1
# Purpose:   converting integers into strings
#
# Author:Joshua Mazurak
#
# Created:09/22/2024
# Licence: CC BY
#-------------------------------------------------------------------------------

# Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday. 
# Write a function which is given the day number, and it returns the day name (a string).



def day_of_the_week (day_call): #defines the name of the function as well as defining the variable of day_call

    if day_call == 0: #checks if the variable of day_call is equal to 0 if it's not the program moves to the next line
        print("sunday")

    elif day_call == 1:   #checks if the variable of day_call is equal to 1 if it's not, 
        print ("mounday") # it moves to the next elif "else-if" statement and continues until it finds a matching variable

    elif day_call == 2:
        print ("tuesday")

    elif day_call == 3:
        print ("wednesday")

    elif day_call == 4:
        print ("thursday")

    elif day_call == 5:
        print ("friday")

    elif day_call == 6:
        print ("saturday")

day_of_the_week(0) #defines what the function is equal to