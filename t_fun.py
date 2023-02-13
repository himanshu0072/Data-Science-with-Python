from turtle import *


def polygon(side, distance):
    for i in range(side):
        fd(distance)
        lt(360/side)


# repetation of code is not good in programming remove it and use loop to reduce code and time
# polygon(3, 100)
# polygon(4, 100)
# polygon(5, 100)
# polygon(6, 100)
# polygon(7, 100)
# polygon(8, 100)

for i in range(3, 11):
    polygon(i, 100)

for i in range(3, 100):
    polygon(3, i*10)
    bk(10)
    bgcolor("black")
    color("yellow")


hideturtle()
mainloop()
