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
        
def check_input():
    tile_num = int(input("Input Number of Tiles: "))
    life_num = int(input("Input Number of Life: "))
    
    #row_num = tile_num
    #col_num = tile_num
    
    if tile_num < 5:
        raise ValueError("Tile number must be greater than 5")
    if not isinstance (life_num, int):
        raise ValueError("Life number must be an integer")
    
    return tile_num, life_num

def main():
    pygame.init()
    
    tile_num, life_num = check_input()
    screen_size = tile_num * 20
    
    screen = pygame.display.set_mode((screen_size, screen_size))
    
    generation = 0
    life = 0
    pygame.display.set_caption("Conway's Game of Life")
    tile_size = screen_size / tile_num
    
    coords_data = set_coords(tile_num, life_num)
    
    # for pos in coords_data:
    #     if coords_data[pos].status:
    #         print(f"Life at {pos}")
    
    clock = pygame.time.Clock()
    
    execute = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #left button add life
                    x, y = event.pos
                    x = x // tile_size
                    y = y // tile_size
                    coords_data[(x, y)].status = True
                    print(f"Life at {x, y}")
                    
                elif event.button == 3: #right button delete life
                    x, y = event.pos
                    x = x // tile_size
                    y = y // tile_size
                    coords_data[(x, y)].status = False
                    print(f"No life at {x, y}")
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Starting Time")
                    if execute == False:
                        execute = True
                    else:
                        execute = False
                        print("Paused")
        
  
        
        screen.fill((0, 0, 0))
        draw_life(screen, tile_size, coords_data)
        draw_grid(screen, tile_size, tile_num)
        
        if execute:
            coords_data = update_coords(coords_data, tile_num)
            generation += 1
        
        pygame.display.flip()
        
        clock.tick(5)  # Adjust the speed as necessary

def draw_grid(screen, size, num):
    for row in range(num):
        for col in range(num):
            rect = pygame.Rect(col*size, row*size, size, size)
            pygame.draw.rect(screen, (5,5,5), rect, 1)
            
def draw_life(screen, size, coords_data):
    for pos in coords_data:
        if coords_data[pos].status:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0]*size, pos[1]*size, size, size))
        elif coords_data[pos].status == False:
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(pos[0]*size, pos[1]*size, size, size))
            
def set_coords(tile_num, life_num):
    coords_data = {}
    for x in range(tile_num):
        for y in range(tile_num):
            coords_data[(x, y)] = Life(x, y, False)
            
    for _ in range(life_num):
        x_pos, y_pos = random.randint(0, tile_num-1), random.randint(0, tile_num-1)
        coords_data[(x_pos, y_pos)] = Life(x_pos, y_pos, True)
            
    return coords_data

def update_coords(coords_data, tile_num):
    offsets = [(0, 1), (0, -1), (1, 0), 
               (-1, 0),         (-1, -1), 
               (1, 1), (-1, 1), (1, -1)]
    
    new_coords_data = coords_data.copy()
    
    for pos in coords_data:
        x, y = pos
        neighbor_count = 0
        
        # Alive current cell
        if coords_data[(x, y)].status:
            for dx, dy in offsets:
                nx, ny = x + dx, y + dy
                if 0 <= nx < tile_num and 0 <= ny < tile_num:  
                    if coords_data[(nx, ny)].status:
                        neighbor_count += 1
            
            if neighbor_count < 2 or neighbor_count > 3:
                new_coords_data[(x, y)].status = False
            
            elif neighbor_count == 2 or neighbor_count == 3:
                new_coords_data[(x, y)].status = True
            
            else:
                new_coords_data[(x, y)].status = False

        # Dead current cell
        if coords_data[(x, y)].status == False:
            for dx, dy in offsets:
                nx, ny = x + dx, y + dy
                if 0 <= nx < tile_num and 0 <= ny < tile_num:  
                    if coords_data[(nx, ny)].status:
                        neighbor_count += 1
                        
            if neighbor_count == 3:
                new_coords_data[(x, y)].status = True
            
    return new_coords_data

if __name__ == "__main__":
    main()