from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# A starting snake, food, and scoreboard is created.
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Initializes the game. Snake begins moving, takes commands, populates food, listens for endgame conditions, and keeps score.
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    snake.reorder()

    # Detect collision between food and snake.
    if snake.head.distance(food) < 12:
        food.refresh()
        score.plus_one()
        snake.extend()

    # Detect collision between head and tail.
    for segment in snake.segments[:-1]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False
    
    # Detect collision between wall and snake.
    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        score.game_over()
        game_is_on = False

screen.exitonclick()