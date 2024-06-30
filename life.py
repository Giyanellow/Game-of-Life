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
    
    if tile_num < 5:
        raise ValueError("Tile number must be greater than 5")
    if life_num < 5:
        raise ValueError("Life number must be greater than 5")
    
    return tile_num, life_num

def main():
    pygame.init()
    
    tile_num, life_num = check_input()
    screen_size = tile_num * 20
    
    screen = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption("Conway's Game of Life")
    tile_size = screen_size / tile_num
    
    coords_data = set_coords(tile_num, life_num)
    for pos in coords_data:
        if coords_data[pos].status:
            print(f"Life at {pos}")
    
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        
        screen.fill((0, 0, 0))
        draw_life(screen, tile_size, coords_data)
        draw_grid(screen, tile_size, tile_num)
        
        coords_data = update_coords(coords_data, tile_num)
        
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
    offsets = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    
    new_coords_data = coords_data.copy()
    
    for pos, life in coords_data.items():
        x, y = pos
        neighbor_count = 0
        
        for dx, dy in offsets:
            nx, ny = x + dx, y + dy
            if 0 <= nx < tile_num and 0 <= ny < tile_num and coords_data[(nx, ny)].status:
                neighbor_count += 1
                    
            #print(f"Neighbor count at {pos}: {neighbor_count}")

            if neighbor_count < 2 or neighbor_count > 3:
                new_coords_data[pos].status = False
            elif neighbor_count > 3:
                new_coords_data[pos].status = False
            elif neighbor_count == 2 or neighbor_count == 3:
                new_coords_data[pos].status = True
            
    return new_coords_data

if __name__ == "__main__":
    main()