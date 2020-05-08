# pong
# @dncnmckn @sprkwd
# using the turtle library

import turtle # for simple games
import os # interact with the operating system using text commands
# import winsound <- windows only sound module

game_window = turtle.Screen()
game_window.title("Pong by @sprkwd ")
game_window.bgcolor("black")
game_window.setup(width=800, height=600)
game_window.tracer(0) # stops window updating so we have to manually update it. Speeds up game.

# Score
score_a = 0
score_b = 0

# paddle A (left)
paddle_a = turtle.Turtle()
paddle_a.speed(0) # set the speed of animation to maximum
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() # turtle draws lines as its moving so this command stops it
paddle_a.goto(-350, 0)

# Paddle B (right)
paddle_b = turtle.Turtle()
paddle_b.speed(0) # set the speed of animation to maximum
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() # turtle draws lines as its moving so this command stops it
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) # set the speed of animation to maximum
ball.shape("circle")
ball.color("white")
ball.penup() # turtle draws lines as its moving so this command stops it
ball.goto(0, 0)

ball.dx = 2 # d is 'delta' or movement. could be anything here doesn't have to be a d could be ball.xspeed = 2
ball.dy = 2

# create a pen (ahem, turtle)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard Bindings
game_window.listen()
game_window.onkeypress(paddle_a_up, "a")
game_window.onkeypress(paddle_a_down, "z")

game_window.onkeypress(paddle_b_up, "'")
game_window.onkeypress(paddle_b_down, "/")

# main game loop (all games need this)
while True:
    game_window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # reverses the direction
        os.system("afplay /Users/dncnmckn/dev/pong/hit.mp3&") # the macOS way of doing it. "aplay" (linux) "". & symbol removes the delay from playing the audio
        # winsound.PlaySound(hit.mp3, winsound.SND_ASYNC) <-- windows version of os.system() SND_ASYNC <- async sound. like & (above)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay /Users/dncnmckn/dev/pong/hit.mp3&") 

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1 # score goes to opposite player
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay /Users/dncnmckn/dev/pong/hit.mp3&") 

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay /Users/dncnmckn/dev/pong/hit.mp3&") 