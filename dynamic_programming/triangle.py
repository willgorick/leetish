import math
# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

def triangle(triangle):
  tri_size = len(triangle)
  dp = [0 for _ in range(tri_size+1)]
  i = tri_size - 1
  while i >= 0:
    for j in range(len(triangle[i])):
      optimal = min(dp[j], dp[j+1])
      dp[j] = triangle[i][j] + optimal
    i -= 1
  return dp[0]
    

def main():
  triangle_arr = [[2], [3,4], [6,5,4], [4,1,8,3]]
  print(triangle(triangle_arr))

main()