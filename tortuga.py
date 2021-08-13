import turtle



window = turtle.Screen()
tortuga = turtle.Turtle()

camino = 0

while camino < 5:
    tortuga.forward(100)
    tortuga.right(90)
    tortuga.forward(100)
    tortuga.left(90)
    camino += 1    

window.mainloop()