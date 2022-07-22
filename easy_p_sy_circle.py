from turtle import *

shape('turtle')
run = True
x= 0
speed(0)

while run:

    forward(100)
    left(7)
    backward(100)
    x += 1
    if x % 1000 == 0:
        run = False
    



mainloop()



