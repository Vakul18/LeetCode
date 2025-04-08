"""
Count lakes in islands


    [0,1,1,1,0],
    [0,1,1,1,0],
    [1,0,0,0,1]
    [1,0,0,0,1],
    [1,0,0,0,1],
    [0,1,1,1,0]



(grid, coord)

iterate all the connected land coords using dfs -> land_coord
store all the neighbouring water cells and also maintain a dict {row, (min_col, max_col)} for each rows land cells

iterate through all the the water cells which are within the land bounds for that row and count the lakes using dfs.


"""
from typing import Set, Tuple

input_grid_1 = [
    [0,0,1,0,0],
    [0,0,1,0,0],
    [1,1,0,1,1],
    [0,0,1,0,0]
]

input_grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,1,1,1,1,1,0,0,0,0,0],
    [0,1,0,0,1,1,0,1,0,1,1,0,0],
    [0,1,1,1,1,1,1,1,0,1,1,0,0],
    [0,0,1,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]





def get_water_coords_within_land_bounds(start_coord : Tuple[int, int], grid: list[list[int]]) -> list[Tuple[int, int]]:
  water_coords = []
  bounds_by_row = dict()
  bounds_by_col = dict()

  stack = [start_coord]
  visited = set()
  while len(stack) > 0:
    coord = stack.pop()

    visited.add(coord)

    drs, dcs = [1,0,-1], [1,0,-1]
    
    for dr in drs:
      for dc in dcs:
        if dr == 0 and dc == 0:
          continue
 
        r,c = coord[0] + dr, coord[1] + dc 
        
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or ((r,c) in visited):
          continue
        
        visited.add((r,c))
        if grid[r][c] == 0:
          water_coords.append((r,c))
        else:
          stack.append((r,c))
          if r in bounds_by_row:
            bounds_by_row[r] = (max(c, bounds_by_row[r][0]), min(c, bounds_by_row[r][1]))
          else:
            bounds_by_row[r] = (c,c)

          if c in bounds_by_col:
            bounds_by_col[c] = (max(r, bounds_by_col[c][0]), min(r, bounds_by_col[c][1]))
          else:
            bounds_by_col[c] = (r,r)
    
  bound_water_coords = []

  for r,c in water_coords:
    bounded_coord = False
      
    if (r in bounds_by_row and bounds_by_row[r][0] >= c and bounds_by_row[r][1] <= c) and  (c in bounds_by_col and bounds_by_col[c][0] >= r and bounds_by_col[c][1] <= r):
      bounded_coord = True       
    
      if bounded_coord:
        bound_water_coords.append((r,c))
  return bound_water_coords  
        
        

def count_lakes(grid : list[list[int]], coord : Tuple[int, int]) -> int:
  water_coords = get_water_coords_within_land_bounds(coord, grid)

  lakes_count = 0
  
  if len(water_coords) > 0:
    visited = set()
    for water_coord in water_coords:
      if water_coord in visited:
        continue
      visited.add(water_coord)
      stack = [water_coord]
      d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
      while len(stack) > 0:
        water_cell = stack.pop()
        

        for dr,dc in d:
          r,c = water_cell[0] + dr, water_cell[1] + dc
        
          if grid[r][c] == 1 or ((r,c) in visited):
            continue

          visited.add((r,c))
          stack.append((r,c))
      lakes_count += 1
      
         
              

  return lakes_count 



print(count_lakes(input_grid, (2,1)))


  