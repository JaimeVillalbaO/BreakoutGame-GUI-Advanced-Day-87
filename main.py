from turtle import Turtle, Screen
from scoreboard import ScoreBoard
from paddle import Paddlee
from bricks import Bricks
from ball import Ball
import time 


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
BRICK_ROW_COLORS = [ "#E3FCBF", "#B8F1B0",  "#14C38E", "#00FFAB"]
level = 0
paddle_len = 7

screen = Screen()
screen.tracer(0)
scoreboard = ScoreBoard()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('BREAKOUT GAME')


paddle = Paddlee(0, -270, stretch_len=paddle_len)

screen.listen()
screen.onkeypress(paddle.go_left, 'Left')
screen.onkeypress(paddle.go_right, 'Right')


def show_bricks():
    global rows_of_bricks
    rows_of_bricks = [[], [], [], []]
    for i, row in enumerate(rows_of_bricks):
        number_of_bricks_per_row = int((SCREEN_WIDTH / 70)) #porque el len del turtle es 3.0 = 30 px left rigt + 10 de espacio
        for each_brick in range(number_of_bricks_per_row):
            x_pos = (SCREEN_WIDTH / 2) - (each_brick * 70) - 50
            brick = Bricks(BRICK_ROW_COLORS[i], xpos=x_pos, ypos=(i * 30) + 100)
            rows_of_bricks[i].append(brick)

show_bricks()
ball = Ball()


game_over = False
while not game_over:
    time.sleep(ball.move_speed)
    screen.update()
    
    ball.move()
    
    # detect a collisiion with wall
    if ball.ycor() > 280 :
        ball.bounce_y()
    if ball.xcor() < -480 or ball.xcor() > 480:
        ball.bounce_x()

    # # detect a collision with a paddle
    if ball.distance(paddle) < 100 and ball.ycor() == -250 :
        ball.detect_paddle()

    # # detect a collision with a bricks
    remaining_bricks = 0
    for row in rows_of_bricks:
        remaining_bricks += len(row)
        for brick in row:
            if ball.distance(brick) < 43 and brick.ycor() - 20 < ball.ycor() < brick.ycor() + 20:
                brick.goto(1000, 0)
                row.remove(brick)
                scoreboard.update_scoreboard()
                ball.bounce_y()
                scoreboard.touch_bricks()
    
    if remaining_bricks == 0:
        level += 1
        show_bricks()
        ball.reset_position()
        paddle.shapesize(1, stretch_len=(paddle_len-level))


    # # detect paddle miss the ball
    if ball.ycor() < -300:
        ball.reset_position()
        if scoreboard.balls_remainging >= 1:
            scoreboard.lose_life()
        else:
            game_over = True
            scoreboard.game_over()



screen.exitonclick()
