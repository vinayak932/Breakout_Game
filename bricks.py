from turtle import Turtle

class Bricks(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.penup()

