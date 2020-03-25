import turtle 

koko = turtle.Turtle()

koko.speed(50)

for i in range(180):
    koko.forward(100)
    koko.right(30)
    koko.forward(20)
    koko.left(60)
   
    
    koko.penup()
    koko.setposition(0, 0)
    koko.pendown()
    
    koko.right(2)
    
turtle.done()
