#-------------------------------------------------------------------------------
# Name:        4.9.2 exercise 2
# Purpose:  use basic turtle functions and create a function to draw a nested square
#
# Author:Joshua Mazurak
#
# Created:09/15/2024
# Licence: CC BY
#-------------------------------------------------------------------------------

import turtle #alows turtle use

rep=1 #variable for repeating amounts 

linesize=20 #size of lines

ang1=135 #variable for angles used to cancel out

def draw_square(t, sz): #creates function to draw squares and moves turtle to next loaction
   
   for i in range(rep*20): #for loop that moves the turtle to next loaction and trigers the for loop to draw square
        
        for i in range(rep*4): #for loop to draw square

            t.forward(sz)
            
            t.right(90)
        
        t.penup() #picks up stylus
        
        t.left(ang1)
        
        t.forward(14)
        
        t.right(ang1)
        
        t.pendown() #puts down stylus
        
        sz =sz+20 # adds size to the var of sz = linesize

    

wn = turtle.Screen() #turtle screen creation
wn.bgcolor("black")
wn.title("I need more sleep")

pen = turtle.Turtle() #creates turtle
pen.color("white")
draw_square(pen , linesize)
pen.speed(0)

wn.mainloop()
