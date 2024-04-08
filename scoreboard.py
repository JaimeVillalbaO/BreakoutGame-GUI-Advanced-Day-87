from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.balls_remainging = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-350, 240)
        self.write(f'SCORE: {self.score}', align = 'center', font= ('Arial', 30, 'normal') )
        self.goto(280, 240)
        self.write(F'BALLS REMAINING: {self.balls_remainging}', align = 'center', font= ('Arial', 30, 'normal') )

    def touch_bricks(self):
        self.score += 10
        self.clear()
        self.update_scoreboard()

    def lose_life(self):
        self.balls_remainging -= 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, -40)
        self.write(f'GAME OVER', align = 'center', font= ('Arial', 80, 'normal') )
