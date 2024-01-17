from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBorad
import time

#Game Setup with Screen Width, Height and Background
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBorad()

#Game Controls, in the four cardinal directions
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

#Game loop, controls all the factors game related
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detects Food Collisions
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detects Wall Colision
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 265 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    #Detects Tail Collision
    for segment in snake.all_segments:
        if snake.head == segment:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()