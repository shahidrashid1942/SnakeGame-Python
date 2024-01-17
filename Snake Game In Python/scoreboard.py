from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", "24", "normal")

class ScoreBorad(Turtle):
    
    def __init__(self):
        """
        Scoreboard setup, alignment, co-ordinates, fontsize and color
        """
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        """
        Updates score by writing a new turtle overlaping the previous one
        """
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """
        Game over sequence, that if triggered writes a new turtel right in the middle
        """
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Increases score by updating the variable and the scoreboard and clearing the previous turtle
        | clear helps the remove the effects of overlapping
        """
        self.score += 1
        self.clear()
        self.update_score()