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
t.ht()  

y = 100  
for color in colors:  
	racer = t.Turtle() 
	racer.color(color)  
	racer.shape('turtle')  
	racer.up()  
	racer.goto(-100, y)  
	racers.append(racer)  
	y -= 20  

racing = True
while racing:
	for racer in racers:
		racer.forward(randint(1,5))
		if racer.xcor() >= 150:
			racing = False

t.done()
