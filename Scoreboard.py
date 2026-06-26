from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
       super().__init__()
       self.color("white")
       self.penup()
       self.hideturtle()
       self.goto(0,200)
       self.score = 0

    def update_score(self):
       self.clear()
       self.write(f"Score: {self.score}", align="center",
                  font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 5
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0,150)
        self.write("GAME OVER", align="center",
                   font=("Arial", 80, "normal"))
        self.goto(0,-120)
        self.write(f"Score: {self.score}", align="center",
                   font=("Arial", 24, "normal"))

    def won(self):
        self.clear()
        self.goto(0, 150)
        self.write("YOU WON", align="center",
                   font=("Arial", 80, "normal"))
        self.goto(0, -120)
        self.write(f"Score: {self.score}", align="center",
                   font=("Arial", 24, "normal"))

