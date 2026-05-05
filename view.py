import os
import pygame as pg
from utils import resource_path
STANDARD_SIZE = (64, 64)


def init_screensettings():
    screen = pg.display.set_mode((512, 700))
    pg.display.set_caption("Mine Sweeper")
    pg.mouse.set_visible(True)
    background = pg.Surface(screen.get_size())
    background = background.convert()
    screen.blit(background, (0,0))
    return screen, background


def load_picture(name):
    # Bare tilføj filnavnet, ikke hele stien – resource_path håndterer det
    path = resource_path("images", name)
    image = pg.image.load(path).convert_alpha()
    image = pg.transform.scale(image, STANDARD_SIZE)
    rect = image.get_rect()
    return image, rect

def load_smiley(name):
    path = resource_path("images", name)
    image = pg.image.load(path).convert_alpha()
    image = pg.transform.scale(image, (2*STANDARD_SIZE[0], 2*STANDARD_SIZE[0]))
    rect = image.get_rect(topleft=(190, 550)) # måske skrive topleft=pos 190, 550
    return image, rect





def picture_array():
    picture_array = {
        #"unopened": load_picture("unopened.png")[0],
        "mine": load_picture("mine.png")[0],
        "empty": load_picture("empty.png")[0],
        "flagged": load_picture("flag.png")[0],
        "unopened": load_picture("unopened.png")[0],
        "numbers": {
            1: load_picture("one.png")[0],
            2: load_picture("two.png")[0],
            3: load_picture("three.png")[0],
            4: load_picture("four.png")[0]
        }
    }
    return picture_array



def draw_cell(surface, cell, picture_array):
    if not cell.is_shown:
        if cell.is_flagged:
            img = picture_array["flagged"]
        else:
            img = picture_array["unopened"]
    elif cell.is_bomb:
        img = picture_array["mine"]

    elif cell.number > 0:
        img = picture_array["numbers"][cell.number]
    else:
        img = picture_array["empty"]

    surface.blit(img, (cell.row*STANDARD_SIZE[0], cell.col*STANDARD_SIZE[0]))


def draw_grid(surface, cell_array, picture_array):
    for row in cell_array:
        for cell in row:
            draw_cell(surface, cell, picture_array)










def draw_smiley(surface, controller):

    if controller.game_state == 1:
        img, rect = load_smiley("happy.png")
    
    elif controller.game_state == 2:
        img, rect = load_smiley("happy.png")
    
    elif controller.game_state == 3:
        img, rect = load_smiley("sunglasses.png")

    elif controller.game_state == 4:
        img, rect = load_smiley("unhappy.png")

    surface.blit(img, rect)


