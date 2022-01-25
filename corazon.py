import turtle

t = turtle.Turtle()
s = turtle.getscreen()

turtle.title('Para mi quesito')
turtle.bgcolor('black')
t.shape('turtle')
t.pencolor('red')


#Dibujo
def curva():
    for i in range(200):
        t.right(1)
        t.forward(1)

def kokoro():
    t.fillcolor('red')
    t.begin_fill()
    t.left(131)
    t.forward(140)
    curva()
    t.left(135)
    curva()
    t.forward(140)
    t.end_fill()
    escribir()


def escribir():
    t.up()
    t.setpos(-70, 108)
    t.down()
    t.color('white')
    t.write('Jonathan y Kevin', font=("Arial", 14, "bold"))
    t.up()
    t.setpos(-110, 108)


kokoro()

turtle.mainloop()

