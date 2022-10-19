from turtle import Turtle
import random
import time



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("White")
        self.shapesize(.5)
        self.penup()
        self.D = 0
        self.direction()
        self.speeds=10


    def direction(self):
        DIRECTION_1 = random.randint(45, 85)
        DIRECTION_2 = random.randint(93, 135)
        DIRECTIONS = (DIRECTION_1, DIRECTION_2)
        DIRECTION = random.choice(DIRECTIONS)
        self.D = DIRECTION
        # self.D = 90.1
        self.seth(self.D)

    def move(self):
        self.forward(self.speeds)

    def bounce_wall_right(self):
        if (self.D > 0 and self.D < 90):
            print(self.D)
            self.D = 180-self.D
            self.seth(self.D)
            print(self.D)
        elif self.D >270 and self.D <360:
            print(self.D)
            self.D = (360-self.D) +180
            self.seth(self.D)
            print(self.D)
    def bounce_wall_left(self):
        if (self.D > 90 and self.D < 180):
            print(self.D)
            self.D = 180-self.D
            self.seth(self.D)
            print(self.D)
        elif self.D > 180 and self.D <270:
            print(self.D)
            self.D = 360-(self.D-180)
            self.seth(self.D)
            print(self.D)

    def bounce_paddle(self):
        print(self.D)
        if self.D > 180 and self.D < 360:
            self.D = 360 - self.D
            self.seth(self.D)
            print(self.D)

    def bounce_blocks(self):
        if self.D > 0 and self.D < 180:
            self.D = 360 - self.D
            self.seth(self.D)
            print(self.D)

    def inc_speed(self):
        self.speeds+=.5

    def ball_reset(self):
        self.home()
        self.direction()
        self.seth(self.D)
        self.move()