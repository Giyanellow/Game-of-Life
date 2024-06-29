import random

def main():
    tile_num = int(input("Enter the number of tiles: "))  # Convert input to integer
    coords = set_coords(tile_num)
    
    print("The coordinates are:", coords)
    
def set_coords(tile_num):
    coords = []
    for x in range(tile_num):
        for y in range(tile_num):  
            coords.append((x, y)) 
    return coords

if __name__ == "__main__":
    main()