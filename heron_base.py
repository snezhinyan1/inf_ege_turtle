from turtle import *

tracer(0)
screensize(10000, 10000)
r = 30

lt(90)

# Команды из условия задачи
# circle(-radius * r, 180) — рисование полуокружности (дуги) по часовой стрелке
# fd(n * r)
# rt(m) / lt(m)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(3, 'red')

update()
done()
