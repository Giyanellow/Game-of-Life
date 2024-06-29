'''
GAME OF LIFE RULES: 

1. Any live cell with fewer than two live neighbors dies as if caused by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
'''

import pygame
import random

class Life:
    def __init__(self, x_pos, y_pos, status):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.status = status

def main():
    pygame.init()
    
    tile_num = int(input("Input Number of Tiles: "))
    life_num = int(input("Input Number of Life: "))
    screen_size = tile_num * 20  # Adjust the scaling factor as needed
    
    screen = pygame.display.set_mode((screen_size, screen_size))
    tile_size = screen_size / tile_num 
    
    grid_data= set_grid(tile_num, life_num)
    
    for pos in grid_data:
        if grid_data[pos] != False:
            print(f"Life at : {pos}")

    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        draw(screen, tile_size, tile_num)
        for pos in grid_data:
            draw_life(grid_data, pos, screen, pygame.Rect(pos[0]*tile_size, pos[1]*tile_size, tile_size, tile_size))
        
        
    clock = pygame.time.Clock()
    clock.tick(5)

def draw(screen, size, num):
    for row in range(num):
        for col in range(num):
            rect = pygame.Rect(col*size, row*size, size, size)
            pygame.draw.rect(screen, (5,5,5), rect, 1)
            
    pygame.display.flip()

def draw_life(grid_data, pos, screen, rect):
    if grid_data[pos] != False:
        pygame.draw.rect(screen, (0, 255, 0), rect)
        
def set_grid(tile_num, life_num):
    grid_data = {}
    for x in range(tile_num):
        for y in range(tile_num):
            grid_data[(x, y)] = False
            
    for _ in range(life_num):
        x_pos = random.randint(0, tile_num-1)
        y_pos = random.randint(0, tile_num-1)
        status = True
        life = Life(x_pos, y_pos, status)
        grid_data[(x_pos, y_pos)] = life
            
    return grid_data

def update_grid(grid_data, tile_num):
    offsets = [(0, 1), (0, -1), (1, 0), 
               (-1, 0),         (-1, -1), 
               (1, 1), (-1, 1), (1, -1)]
    
    new_grid_data = grid_data.copy()
    
    for pos in grid_data:
        x, y = pos
        neighbor_count = 0
        
        for dx, dy in offsets: #dx, dy is the offset coords
            nx , ny = x + dx, y + dy # nx, ny is the original coords + offset
            
            if 0 < nx < tile_num and 0 < ny < tile_num:
                if grid_data[(nx, ny)] != False:
                    neighbor_count += 1
        
        if neighbor_count < 2 or neighbor_count > 3:
            new_grid_data[pos] = False
        
        elif neighbor_count == 3:
            new_grid_data[pos] = Life(x, y, True)
                    
    return new_grid_data


if __name__ == "__main__":
    main()
