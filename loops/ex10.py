from turtle import *

for i in range(6):
    #if i ==5:
       # continue/#break (if we using break else part will not be run
       # if we use continue else part will run)
    fd(150)
    lt(60)
else:
    penup()
    #home() go to center again
    goto(75,75)
    write('Hexagone', align='center')

    

hideturtle()
mainloop()    