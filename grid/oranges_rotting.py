from collections import deque

def orangesRotting(grid):
  q = deque()
  time, fresh = 0, 0

  ROWS, COLS = len(grid), len(grid[0])
  directions = [[0,1], [0,-1], [1,0], [-1,0]]
  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] == 1:
        fresh += 1
      elif grid[r][c] == 2:
        q.append([r, c])
      
  while q and fresh > 0:
    for _ in range(len(q)): #initial length of queue before we add stuff below, this ensures that for each time period we only evaluate the paths from the oranges that were rotten when it started
      r, c = q.popleft()
      for dr, dc in directions:
        row, col = dr + r, dc + c
        if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1:
          grid[row][col] = 2
          q.append([row, col])
          fresh -= 1
    time += 1

  return time if fresh == 0 else -1 #return -1 if unable to rot all oranges

def main():
  print(orangesRotting([[2,2],[1,1],[0,0],[2,0]]))
  print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
main()