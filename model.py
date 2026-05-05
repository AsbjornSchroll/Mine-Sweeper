# I den her fil definerer jeg spillets initial state og alle de forskellige funktioner som spilleren kan udføre
# Logikken for hvor alle tal og bomber bliver placeret, bliver defineret her
import random
from collections import deque
class Cell:
    def __init__(self, col: int, row: int):
        self.row = row
        self.col = col
        self.is_first_field = False
        self.is_flagged = False
        self.is_bomb = False
        self.is_shown = False
        self.number = 0







class Grid:
    def __init__(self, grid_size):
        self.cell_array = [[Cell(col, row) for col in range(grid_size)] for row in range(grid_size)] # initialiserer grid med celler der har features som er defineret i Cell



    def get_cell_from_pos(self, pos):

        mouse_col, mouse_row = pos

        col = mouse_col//64
        row = mouse_row//64

        cell = self.cell_array[col][row]

        return cell
    
    def is_mouse_in_grid(self, pos):
        mouse_col, mouse_row = pos
        col = mouse_col//64
        row = mouse_row//64
        array_lenght = len(self.cell_array)
        if 0 <= col < array_lenght and 0 <= row < array_lenght:

            return True
        
        return False



    def flag_cell(self, cell): # Jeg ændrer is_flagged for cellen med koordinaterne cy, cx
        cell.is_flagged = True


    def unflag_cell(self, cell):
        cell.is_flagged = False

    def is_flagged(self, cell):
        if cell.is_flagged:
            return True
        else:
            return False


    def is_shown(self, cell):
        if cell.is_shown:
            return True
        else:
            return False
    
    def is_bomb(self, cell):
        if cell.is_bomb:
            return True
        else:
            return False
        
    
    def show_cell(self, cell): # Jeg ændrer is_shown for cellen med koordinaterne cy, cx
        cell.is_shown = True
 

    def get_cell_number(self, cell):
        return cell.number
    


    def get_cell_neighbours(self, cell):
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        cell_neighbours = []
        rows = len(self.cell_array)
        cols = len(self.cell_array[0]) 
        for j in range(len(offsets)):
            dcol = offsets[j][0]    
            drow = offsets[j][1]

            n_col = cell.col + dcol

            n_row = cell.row + drow
     
            if 0 <= n_row < rows and 0 <= n_col < cols:

                neighbour_cell = self.cell_array[n_row][n_col]

                cell_neighbours.append(neighbour_cell)


        return cell_neighbours




    
    def show_all_cell_neighbours(self, cell):

        neighbours = self.get_cell_neighbours(cell)

        for neighbour in neighbours:
            if neighbour.number == 0:
                self.show_neighbour_numbers(neighbour)

            if not self.is_shown(neighbour) and not self.is_flagged(neighbour):
                self.show_cell(neighbour)


    def fill_bomb_array(self, first_cell):
        n_bombs = 10
        bombs = set() # A set make sure all the elements are unique


        while len(bombs) < n_bombs:
            bomb_row = random.randint(0,7)
            bomb_col = random.randint(0,7)

            if abs(bomb_row-first_cell.row) <= 1 and abs(bomb_col-first_cell.col) <= 1:
                continue

            bombs.add((bomb_row, bomb_col))

        for bomb_row, bomb_col in bombs:
            cell = self.cell_array[bomb_row][bomb_col]
            cell.is_bomb = True
            cell.number = -1
        return list(bombs)





    def fill_numbers_bombs(self, first_cell):
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        rows = len(self.cell_array)
        cols = len(self.cell_array[0])
        bomb_array = self.fill_bomb_array(first_cell)

        for k in range(len(bomb_array)):
            for j in range(8):
                d_row = offsets[j][0]
                d_col = offsets[j][1]
                bomb_row = bomb_array[k][0]
                bomb_col = bomb_array[k][1]
                n_row = bomb_row+d_row
                n_col = bomb_col+d_col
                if 0 <= n_row < rows and 0 <= n_col < cols:
                    neighbour_cell = self.cell_array[n_row][n_col]
                    if not neighbour_cell.is_bomb:
                        neighbour_cell.number += 1
                        #neighbour_cell.is_shown = True






    def get_bombs_in_neighbours(self, cell):

        neighbours = self.get_cell_neighbours(cell)
        num_bombs = 0
        for neighbour in neighbours:

            if neighbour.is_bomb == True:
                num_bombs += 1

        return num_bombs


    def show_neighbour_numbers(self, first_cell):


        if first_cell.is_bomb:
            return
        
        if first_cell.number > 0:

            if self.number_match_neighbour_bombs(first_cell):

                self.show_all_cell_neighbours(first_cell)

        
        if first_cell.number == 0:

            q = deque([first_cell]) # Et deque array, der holder den første celle

            visited = {(first_cell.row, first_cell.col)} # Et array der skal holde de besøgte celler

            while q:

                cell = q.popleft()
                neighbours = self.get_cell_neighbours(cell)

                for n in neighbours:
                    
                    if not n.is_shown:
                        n.is_shown = True

                    key = (n.row, n.col)

                    if n.number == 0 and key not in visited:

                        visited.add(key)

                        q.append(n)
        
                        
    def number_match_neighbour_bombs(self, cell):

        cell_neighbours = self.get_cell_neighbours(cell)

        flagged_bombs = 0

        for neighbour in cell_neighbours:

            if self.is_flagged(neighbour) and self.is_bomb(neighbour):
                flagged_bombs += 1 

        if flagged_bombs == cell.number:

            return True
        
        return False
    
    def clear_all_cells(self):
        for col in self.cell_array:
            for cell in col:
                cell.is_first_field = False
                cell.is_flagged = False
                cell.is_bomb = False
                cell.is_shown = False
                cell.number = 0                      

    def is_game_won(self):
        count = len(self.cell_array)**2
        done_cells = 0
        for col in self.cell_array:
            for cell in col:
                if cell.is_shown or (cell.is_flagged and cell.is_bomb):
                    done_cells += 1
        if count == done_cells:

            return True
        
        return False
    