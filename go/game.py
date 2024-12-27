import pygame as pg
from classes import Game

game = Game(size = 19)
game.fill_screen()
game.draw()
is_running = True

while is_running:
    is_running = game.update()
    pg.time.wait(60)