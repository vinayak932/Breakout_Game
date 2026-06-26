import time
import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from Scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height = 600)
screen.bgcolor('black')
screen.title('Breakout')
screen.tracer(0)

paddle = Paddle((0,-250))
ball = Ball()
scoreboard = Scoreboard()

game_on = True

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")
ball.start()
bricks = []


start_x = -380
start_y = 150

for row in range(8):
    for col in range(20):
       brick = Bricks()
       x = start_x + col * 43
       y = start_y - row * 30
       brick.goto(x, y)
       if row < 2:
           brick.color('red')
       elif row < 4:
           brick.color('blue')
       elif row < 6:
           brick.color('yellow')
       else:
           brick.color("green")

       bricks.append(brick)

def move_paddle(event):
    x_event = event.x - 400
    paddle.goto(x_event, paddle.ycor())

canvas = screen.getcanvas()
canvas.bind("<Motion>", move_paddle)


while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.xcor() > 380 or ball.xcor() < -380  :
       ball.setx(379)
       ball.bounce_x()
    elif  ball.ycor() > 280 :
        ball.sety(279)
        ball.bounce_y()

    if ball.distance(paddle) < 40 and ball.y_move < 0:
        difference = ball.xcor() - paddle.xcor()
        ball.x_move = difference / 5
        ball.bounce_y()

    if ball.ycor() < -300:
       scoreboard.game_over()
       game_on = False
       break

    if len(bricks) == 0:
        scoreboard.won()
        game_on = False
        break

    for brick in bricks:
        if ball.distance(brick) < 25:
            dx = ball.xcor() - brick.xcor()
            dy = ball.ycor() - brick.ycor()
            if abs(dx) > abs(dy):
                ball.bounce_x()
                scoreboard.increase_score()
            else:
                ball.bounce_y()
                scoreboard.increase_score()

            ball.move_speed *= 0.99

            brick.hideturtle()
            bricks.remove(brick)
            break

screen.exitonclick()

