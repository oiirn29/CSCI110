#-------------------------------------------------------------------------------
# Name:        6.9. exercise 7
# Purpose:   create a function that converts hours mins and seconds into total of seconds 
#
# Author:Joshua Mazurak
#
# Created:09/29/2024
# Licence: CC BY
#-------------------------------------------------------------------------------

"""Write a function to_secs that converts hours, minutes and seconds 
    to a total number of seconds. Here are some tests that should pass:"""
        #test(to_secs(2, 30, 10) == 9010)
        #test(to_secs(2, 0, 0) == 7200)
        #test(to_secs(0, 2, 0) == 120)
        #test(to_secs(0, 0, 42) == 42)
        #test(to_secs(0, -10, 10) == -590)

def to_secs (hours, minutes, seconds):      #creates a function that contains the math protion of the exercise

    hours2 = hours * 60*60          #defines what the veriable of hours2 is equal to

    minutes2 = minutes * 60         #defines what the veriable of minutes2 is equal to

    total_seconds = hours2 + minutes2 + seconds         #defines what the veriable of total_seconds is equal to

    return total_seconds

import sys          #imports system log/output 

def test(did_pass):         #creates the function test that calls out the line number, 
                            #and checks if the math in the test area works against the "to_secs function"
   
    linenum = sys._getframe(1).f_lineno   # fetch the line number.

    if did_pass:            #action if the test was successful

        msg = "Test at line {0} Success.".format(linenum)

    else:           #action if the test failed

        msg = ("Test at line {0} Failure.".format(linenum))

    print(msg)          #prints the returned value 


def test_suite():           #creates the function that contains all the test parameters

    test(to_secs(2, 30, 10) == 9010)

    test(to_secs(2, 0, 0) == 7210)

    test(to_secs(0, 2, 0) == 120)

    test(to_secs(0, 0, 42) == 42)

    test(to_secs(0, -10, 10) == 2590)
    
test_suite()            #tells python to run the function which cascades backwards to complete the program


