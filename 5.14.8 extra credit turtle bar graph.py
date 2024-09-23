#-------------------------------------------------------------------------------
# Name:        5.14 exercise 8
# Purpose:   create a bar graph that uses turtles to dispay the out put
#
# Author:Joshua Mazurak
#
# Created:09/22/2024
# Licence: CC BY
#-------------------------------------------------------------------------------
# 5.14.7 cuz it looks better. "Modify the turtle bar chart program so that the pen is up for the small gaps between each bar."
# 5.14.8 Modify the turtle bar chart program so that the bar for any value of 200 or more is filled with red, 
# values between [100 and 200) are filled with yellow, and bars representing values less than 100 are filled with green.

import turtle #alows turtle use



def draw_bar(t, height): #defines the instructions to draw the bars 

    barfill(t, height) #calls the barfill definition to set the fill color 

    t.pendown()     # puts down tess

    t.begin_fill()           #starts the filling of last shape

    t.left(90)
    t.forward(height)

    t.write("  "+ str(height)) #writes the variable used of the height of the bar above the bar 
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)

    t.end_fill()            #ends the filling of last shape

    t.penup()             # picks up tess

    t.forward(10)

def barfill(t, height):     #defines the color of the bar based on the height of the bar 

    if height < 100:        # changes color to green if hieght is less then 100
        t.fillcolor("green") 

    elif height < 200:      # changes color to yellow if hieght is less then 200
        t.fillcolor("yellow")
        
    else:                   #changes color to red if hieght is more then 200
        t.fillcolor("red")

wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgrey")
wn.title("I need more sleep")


tess = turtle.Turtle()       # Create tess and set some attributes
tess.color("black")
tess.pensize(0)
tess.speed(0)
tess.penup()
tess.backward(180)
tess.pendown()

xs = [48,117,200,240,160,260,220] #assinges the bar values to xs

for a in xs:    #sets for loop to draw the bars as defined in the draw_bar and the xs variable
    draw_bar(tess, a)

wn.mainloop()