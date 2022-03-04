from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 15, "normal")
TOP = 275
MIDDLE = 0

class Score(Turtle):
    

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.current_score = 0
        self.write_score()


    def write_score(self):
        self.setpos(MIDDLE, TOP)
        self.write(arg = f"Score : {self.current_score}", move = True, align = ALIGN, font = FONT)


    # Updates score when a food is eaten.
    def plus_one(self):
        self.clear()
        self.current_score += 1
        self.write_score()

    def game_over(self):
        self.home()
        self.write(arg = "Game Over", align = ALIGN, font = FONT)
        
