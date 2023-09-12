from turtle import *

#data=[2,50,35,68,90,6,45,82]
data=[1,20]
vb=[360]
goto(200,200)
for val in data :
    fd(val)
    lt(360/6)
    circle(val,180)
    #write(val)
hideturtle()
mainloop()    