from turtle import*
speed('fastest')
goto(0,0)
pensize(4)

move=5
while True:

    fillcolor('yellow')
    begin_fill()
    for i in range(6):
        fd(100+move)
        rt(60)
        fillcolor('blue')
        begin_fill()
        for i in range(6):
           fd(50)
           rt(60)
        end_fill() 
    end_fill()  
    rt(60)
    move+=5
       
  
hideturtle()
mainloop()        