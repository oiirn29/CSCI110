#-------------------------------------------------------------------------------
# Name:        19.6 exercise 1
# Purpose:   prompt the user for a positive integer and then checks if output is correct 
#
# Author: Joshua Mazurak
#
# Created:11/10/2024
# Licence: CC BY
#-------------------------------------------------------------------------------


def readposint ():      #deffines the steps

    data = input("Please enter your int: ")         #user prompt 

    try:            #attempts to complete code inside this area

        data = int(data)        #converts all input into an intager

        if data <= 0:       #checks if it's less then ore equal to 0 

            my_error = ValueError("> {0} < is not an interger ".format(data))       #costom error mesg

            raise my_error          #calls the costom error mesg
        
        elif data >= 1:          #checks if it's more then or equal to 1

            print("> {0} < is a positive interger ".format(data))       #outputs it is a positive int 
        

    except ValueError:      #catches error and give custom error 

        print("> {0} < is not an interger ".format(data))

readposint()        #calls def