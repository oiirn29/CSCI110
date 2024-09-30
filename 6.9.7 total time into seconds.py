#-------------------------------------------------------------------------------
# Name:        5.14 exercise 8
# Purpose:   create a bar graph that uses turtles to dispay the out put
#
# Author:Joshua Mazurak
#
# Created:09/22/2024
# Licence: CC BY
#-------------------------------------------------------------------------------

"""Write a function to_secs that converts hours, minutes and seconds 
    to a total number of seconds. Here are some tests that should pass:"""

#test(to_secs(2, 30, 10) == 9010)
#test(to_secs(2, 0, 0) == 7200)
#test(to_secs(0, 2, 0) == 120)
#test(to_secs(0, 0, 42) == 42)
#test(to_secs(0, -10, 10) == -590)

def to_secs (h, m, s):
    h2= h * 60*60
    m2 = m * 60
    total_seconds = h2 + m2 + s 
    return total_seconds

import sys

def test(did_pass):
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} Success.".format(linenum)
    else:
        msg = ("Test at line {0} Failure.".format(linenum))
    print(msg)


def test_suite():

    test(to_secs(2, 30, 10) == 9010)

    test(to_secs(2, 0, 0) == 7200)

    test(to_secs(0, 2, 0) == 120)

    test(to_secs(0, 0, 42) == 42)

    test(to_secs(0, -10, 10) == -590)
    
test_suite() 



