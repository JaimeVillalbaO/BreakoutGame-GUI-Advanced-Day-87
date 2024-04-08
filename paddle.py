from turtle import Turtle, Screen


class Paddlee(Turtle):

    def __init__(self, x_cor, y_cor, stretch_len):
        super().__init__()
        self.shape('square')        
        self.color('white')
        self.shapesize(1, stretch_len=stretch_len)
        self.penup()
        self.goto(x=x_cor, y=y_cor)

    def go_left(self):
        if self.xcor() < -430:
            pass
        else: 
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())

    def go_right(self):
        if self.xcor() > 410:
            pass
        else: 
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())

     
