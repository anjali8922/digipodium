from turtle import *

speed('fastest')
bgcolor('green')
pencolor('yellow')
pensize(4)
#goto(-250,250)

for i in range(1,1000,5):
    fd(i)
    lt(360/5)
    write(i)
hideturtle()
mainloop()    