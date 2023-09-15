from turtle import *
speed('fastest')
dis=[100,100,100,100,100,90,60,40,60,280,100,330,100,330,100,100,190]
ngl=[90,45,90,45 ,90,90,90,90,90,90,90,90,90,90,45,45,20]
#goto(50,30)
bgcolor('powderblue')
pencolor('black')
pensize(6)
#fillcolor('brown')

#begin_fill()

for d,a in zip(dis,ngl) :
    fd(d)
    lt(a)
    #fd(50)
    #lt(90)
    #goto(250,-50)
  
  #  fd(50)
   # lt(90)

    #rt(a)
    #fd(d)
    #lt(a)
#end_fill() 

penup()
goto(183,75)
right(20)
pendown()   
for i in range(2):
    fd(50)
    lt(90)
    fd(50)
    lt(90)
hideturtle()
mainloop()    