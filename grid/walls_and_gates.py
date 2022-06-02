# Given a maze with cells being: gates, walls or empty spaces.

# Fill the empty spaces with the number of steps to the closest gate. Allowed steps: UP, RIGHT, LEFT & DOWN

import math
from collections import deque

def walls_and_gates(grid):
  row_len = len(grid)
  col_len = len(grid[0])
  q = deque()
  directions = [[0,1], [0,-1], [1,0], [-1,0]]
  for i in range(row_len):
    for j in range(col_len):
      if grid[i][j] == 0:
        q.append([i, j, 1])
      
  while q:
    i, j, count = q.popleft()
    for x, y in directions:
      row = i+x
      col = j+y
      if 0 <= row < row_len and 0 <= col < col_len and grid[row][col] != -1:
        if grid[row][col] == math.inf: #only update if not updated yet
          grid[row][col] = count
          q.append([row, col, count+1])

  return grid



def main():
  grid1 = [[math.inf, -1, 0, math.inf], [math.inf, math.inf, math.inf, -1], [math.inf, -1, math.inf, -1], [0, -1, math.inf, math.inf]]
  solved_grid = walls_and_gates(grid1)
  for row in solved_grid:
    print(row)
main()