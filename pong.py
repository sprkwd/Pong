# pong
# @dncnmckn @sprkwd

import turtle # for simple games

game_window = turtle.Screen()
game_window.title("Pong by @sprkwd ")
game_window.bgcolor("black")
game_window.setup(width=800, height=600)
game_window.tracer(0) # stops window updating so we have to manually update it. Speeds up game.

# paddle A (left)
paddle_a = turtle.Turtle()
paddle_a.speed(0) # speed of animation... MAXimim
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup() # turtle draws lines as its moving
paddle_a.goto(-350, 0)

# Paddle B (right)


# Ball

# main game loop (all games need this)
while True:
    game_window.update()
