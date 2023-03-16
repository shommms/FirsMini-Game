import turtle as t
from random import randint

racers = []
colors = ["red", "blue", "green", "yellow", "purple", "magenta", 'pink']

t.up()
t.goto(150, 110)
t.down()
t.goto(150, -40)
t.up()
t.goto(0,0)
t.ht()  # прячем черепаху которая рисует финишную черту

y = 100  # объявляем начальную координату по высоте
for color in colors:  # для каждого цвета
	racer = t.Turtle()  # создаём объект гонщика
	racer.color(color)  # устанавливаем цвет гонщику
	racer.shape('turtle')  # говорим, что форма нашего гонщика - черепаха
	racer.up()  # поднимаем перо, чтобы гонщик не оставлял след при движении
	racer.goto(-100, y)  # перемещаем гонщика на линию старта
	racers.append(racer)  # добавляем гонщика в список наших участников racers
	y -= 20  # изменяем координату y для следующего гощика

racing = True
while racing:
	for racer in racers:
		racer.forward(randint(1,5))
		if racer.xcor() >= 150:
			racing = False

t.done()
