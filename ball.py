from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()    
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x = 5
        self.y = 5
        self.move_speed = 0.05
    
    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.y *= -1
    
    def bounce_x(self):
        self.x *= -1

        

    def detect_paddle(self):
        self.y *= -1
        self.move_speed *= 0.8
        bounce = random.randint(0,1)
        if bounce == 1:
            self.x *= -1


    def reset_position(self):
        self.goto(0 , 0)
        self.move_speed = 0.05
        self.detect_paddle()