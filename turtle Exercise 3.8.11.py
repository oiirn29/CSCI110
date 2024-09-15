import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
wn.bgcolor("teal")
alex = turtle.Turtle()    # Create a turtle, assign to alex

alex.speed(0)

la=200 # la is the var for the langth of stright runs

ang1=144 # ang1 is var for one angle.... 144 is *magic*

for pain in range(30):
    alex.right(ang1)

    alex.forward(la)

    alex.right(ang1)

    #alex.forward(la)


wn.mainloop()             # Wait for user to close window