import turtle 

my_turtle = turtle.Turtle()
my_turtle.speed(0)

def square(length, angle):
    for k in range(4): 
       my_turtle.forward(length)
       my_turtle.right(angle)

for k in range(23):   
    square(100, 90)
    my_turtle.right(15)
    square(100, 90)
