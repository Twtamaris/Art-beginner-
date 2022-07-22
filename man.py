from turtle import *

run = True
shape('turtle')
x= 0
speed(0)
left(90)
a = 100

while run:
    
   
    forward(a)
    left(30)
  
    a = a * 0.8
    
    x += 1
    
    
    

    if x == 5:
        run = False
     
run  = True
x = 0
a = a/0.8

while run:
    right(30)
    backward(a)
    right(60)
    forward(a)
    backward(a)
    a = a/0.8
    
      
    
    x += 1
    
    if x ==  5:
        run = False




mainloop()




