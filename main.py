import pygame as pg

pg.init()

from model import Grid

from view import init_screensettings, draw_grid, picture_array, draw_smiley

screen, background = init_screensettings()


from controller import Controller

screen, background = init_screensettings()
pictures = picture_array()

grid = Grid(8)
controller = Controller(grid)



running = True
while running:

    running = controller.handle_events()

    draw_grid(screen, grid.cell_array, pictures)
    draw_smiley(screen, controller)

    pg.display.flip()

