# I den her fil, bliver input fra brugeren håndteret.
# Handlinger fra brugeren bliver indsamlet og gemt i et event array.
# Dette event array bliver brugt til at opdatere alle spillets felter
import pygame as pg

from view import load_smiley

_, smiley_rect = load_smiley("happy.png")

def smiley_hit(smiley_rect, pos):
    if smiley_rect.collidepoint(pos):
        return True
    else:
        return False
    


class Controller:
    def __init__(self, grid):
        self.grid = grid # Controller klassen "låner" grid klassen men ejer den ikke. Den ved ikke den eksisterer og at det er en klasse før vi kalder den i main
        self.game_state = 1 # game_state bestemmer hvilken event funktion vi kalder i while loopet i main


    def handle_events_start(self):

        running = True

        self.grid.clear_all_cells()

        for event in pg.event.get():

            if event.type == pg.QUIT:
                running = False
            
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1: # Presser en mousepad ned

                pos = pg.mouse.get_pos() # får positionen

                if self.grid.is_mouse_in_grid(pos):

                    first_cell = self.grid.get_cell_from_pos(pos) # Omdanner position til x og y koordinater

                    self.grid.show_cell(first_cell)

                    self.grid.fill_numbers_bombs(first_cell)

                    self.grid.show_neighbour_numbers(first_cell)

                    self.game_state += 1

        return running
    

    def handle_events_ongoing(self):

        running = True

        if self.grid.is_game_won():

            self.game_state = 3
            return running
        
        for event in pg.event.get():

            if event.type == pg.QUIT:

                running = False

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1: # Presser en mousepad ned
                
                pos = pg.mouse.get_pos()

                if smiley_hit(smiley_rect, pos):
                    self.game_state = 1
                    return running
                

                if self.grid.is_mouse_in_grid(pos):

                    cell = self.grid.get_cell_from_pos(pos)
                    
                    if not self.grid.is_shown(cell):
                        self.grid.show_cell(cell)
                    
                    if self.grid.is_bomb(cell):
                        self.game_state = 4
                        return running
                    

            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:

                pos = pg.mouse.get_pos()

                if self.grid.is_mouse_in_grid(pos):
                    
                    cell = self.grid.get_cell_from_pos(pos)

                    if self.grid.is_shown(cell):

                        if self.grid.number_match_neighbour_bombs(cell):
                
                            self.grid.show_neighbour_numbers(cell)


                    elif not self.grid.is_shown(cell):

                        if self.grid.is_flagged(cell):

                            self.grid.unflag_cell(cell)
                        else:
                            self.grid.flag_cell(cell)
                    

        return running



    def handle_events_game_won(self):
        running = True
        for event in pg.event.get():

            if event.type == pg.QUIT:
                running = False

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:

                pos = pg.mouse.get_pos()

                if smiley_hit(smiley_rect, pos):
                    self.game_state = 1

                    return running
        return running




    def handle_events_game_over(self):
        running = True
        for event in pg.event.get():

            if event.type == pg.QUIT:
                running = False

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:

                pos = pg.mouse.get_pos()

                if smiley_hit(smiley_rect, pos):
                    self.game_state = 1

                    return running
        return running     


    def handle_events(self):
        if self.game_state == 1:
            return self.handle_events_start()
        elif self.game_state == 2:
            return self.handle_events_ongoing()
        elif self.game_state == 3:
            return self.handle_events_game_won()
        elif self.game_state == 4:
            return self.handle_events_game_over()


