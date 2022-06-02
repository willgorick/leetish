# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

from typing import List

class Solution:
  def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    if not heights: 
      return []
    self.directions = [(1,0), (-1,0), (0,1), (0,-1)]
    m = len(heights)
    n = len(heights[0])
        
    pac_visited = [[False for _ in range(n)] for _ in range(m)]
    atl_visited = [[False for _ in range(n)] for _ in range(m)]
    result = []
        
    #these two for loops start from all edge nodes
        
    #left and right edges
    for i in range(m):
      self.dfs(heights, i, 0, pac_visited, m, n)
      self.dfs(heights, i, n-1, atl_visited, m, n)
        
    #top and bottom edges
    for j in range(n):
      self.dfs(heights, 0, j, pac_visited, m, n)
      self.dfs(heights, m-1, j, atl_visited, m, n)
        
    for i in range(m):
      for j in range(n):
        if pac_visited[i][j] and atl_visited[i][j]:
          result.append([i,j])
    return result

  def dfs(self, heights, i, j, visited, m, n):
    visited[i][j] = True
    for dir in self.directions:
      x, y = i+dir[0], j+dir[1]
      if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or heights[x][y] < heights[i][j]: #check if either index is out of bounds, if it has already been visited, or if it is greater than the coordinate we started from
        continue
      self.dfs(heights, x, y, visited, m, n)

def main():
  solution = Solution()
  grid1 = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
  print(solution.pacificAtlantic(grid1))

main()