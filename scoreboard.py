from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(x=0, y=265)
        self.color("white")
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 24, 'normal'))
        self.hideturtle()

    def eat_food(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 24, 'normal'))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", move=False, align='center', font=('Arial', 24, 'normal'))