import turtle
# negyzet rajzolasa
lepes = 1
while lepes <= 4:
    turtle.forward(200)
    turtle.right(90)
    lepes += 1
#otszog
lepes = 1
while lepes <= 5:
    turtle.forward(200)
    turtle.right(72)
    lepes += 1

#6-10 szog
for x in range(6, 11):
    lepes = 1
    while lepes <= x:
        turtle.forward(100)
        turtle.right(360 / x)
        lepes += 1

szog = int(input('szog? '))
lepes = 1
while lepes <= szog:
    turtle.forward(100)
    turtle.right(360 / szog)
    lepes += 1
