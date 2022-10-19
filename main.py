from turtle import *
from paddle import Paddle
from boxes import Boxes
from scoreboard import Scoreboard
from ball import Ball
import time

########## SCREEN ##########
screen = Screen()
screen.bgcolor("black")
screen.setup(width=770, height=1000)
screen.title("BREAKOUT")
screen.tracer(0)

########## PADDLE ##########
paddle = Paddle((0, -450))
screen.listen()
screen.onkey(paddle.go_left, "a")
screen.onkey(paddle.go_right, "d")

########## BOXES ##########
box = Boxes()
box.create_boxes()
box.draw_boxes()
########## SCORE ##########
score = Scoreboard()

ball = Ball()
timer_start = time.time()


game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.05)
    ball.move()
    #Detect collision with paddle
    if ball.distance(paddle) < 36:
        ball.bounce_paddle()
    #detect bounce off wall
    if ball.xcor() > 370:
        ball.bounce_wall_right()
    if ball.xcor() < -370:
        ball.bounce_wall_left()
    #detect bounce off blocks
    indx = 0
    for bx in box.all_boxes:
        end = time.time()
        time_dif = end-timer_start
        # print(type(bx))
        if bx.distance(ball) < 38 and time_dif >.5:
            ball.bounce_blocks()
            score.increase_score()
            print(f'index" {indx}')
            print(box.all_boxes[0])
            box.delete_box(indx)
            # box.draw_boxes()
            ball.inc_speed()
            timer_start = time.time()
        indx+=1
    # detect Hitting bottom
    if ball.ycor() < -490:
        score.game_over()
        time.sleep(5)
        break






screen.exitonclick()