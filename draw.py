from turtle import Turtle


class Marker(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def paint(self, x, y, state):
        self.goto(x, y)
        self.write(state, align="center", font=("Ariel", 10, "normal"))
