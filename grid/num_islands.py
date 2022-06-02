#Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

from collections import deque

def num_islands(grid):
  i_len = len(grid)
  if i_len < 1:
    return 0
  j_len = len(grid[0])
  check_queue = deque()
  island_count = 0 
  directions = [(0,1), (0,-1), (1, 0), (-1,0)]

  for i in range(i_len):
    for j in range(j_len):
      if grid[i][j] == "1":
        check_queue.append((i, j))
        grid[i][j] = "-1" #mark that we've already visited this point
        while check_queue:
          (curr_i, curr_j) = check_queue.popleft()
          for direction in directions:
            i_check = curr_i + direction[0]
            j_check = curr_j + direction[1]
            if 0 <= i_check < i_len and 0 <= j_check < j_len and grid[i_check][j_check] == "1":
              grid[i_check][j_check] = "-1"
              check_queue.append((i_check, j_check))
        #once we finish the while loop we've found one island
        island_count += 1
  return island_count




def main():
  grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
  print(num_islands(grid))

  grid2 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]

  print(num_islands(grid2))

main()