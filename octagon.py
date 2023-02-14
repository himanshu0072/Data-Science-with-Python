from turtle import *

side=8
for i in range(side):
    pencolor('blue')
    fd(100)
    lt(360/side)
    pencolor('red')
    dot(30)
mainloop()
