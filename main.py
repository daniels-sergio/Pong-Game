import turtle
from turtle import Screen,Turtle
import time
from paddles import *
from ball import *
from scoreboard import *

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

screen.title("Pong")

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()
paused = False


def pause_game():
    global paused
    paused = not paused

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")



game_on = True
while game_on:
    screen.onkey(pause_game, "space")

    if not paused:
        ball.move()
        screen.listen()
        r_paddle.CanMove = True
        l_paddle.CanMove = True
    else:
        r_paddle.CanMove = False
        l_paddle.CanMove = False






    time.sleep(ball.move_speed)
    screen.update()

    #detect collsion with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()




    #detect collision with paddles

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #detect when ball misses paddle

    if ball.xcor() >= 380:
        ball.reset_position()
        scoreboard.l_point()



    elif ball.xcor() <= -380:
        ball.reset_position()
        scoreboard.r_point()










screen.exitonclick()
