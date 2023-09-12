from turtle import *
speed('slowest')
dis=[100,90,90,100,]
ngl=[90,45,45,45 ,]
#goto(50,30)

for d,a in zip(dis,ngl) :
    fd(d)
    lt(a)
    #fd(d)
    #lt(a)
hideturtle()
mainloop()    