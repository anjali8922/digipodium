from turtle import *

speed('fastest')
bgcolor('green')
pencolor('yellow')
pensize(4)
#goto(-250,250)

for i in range(100,0,-6):
    fd(i)
    lt(360/4)
    write(i)
    circle(i)
hideturtle()
mainloop()    

