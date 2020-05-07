# pong
# @dncnmckn @sprkwd

import turtle

game_window = turtle.Screen()
game_window.title("Pong by @sprkwd ")
game_window.bgcolor("black")
game_window.setup(width=800, height=600)
game_window.tracer(0) # stops window updating so we have to manually update it. Speeds up game.

# main game loop (all games need this)
while True:
    game_window.update()