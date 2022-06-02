#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

def trap(heights) -> int:
  s = 0
  l, r = 0, len(heights)-1
  while l < r:
      i = 1
      if heights[l] < heights[r]:
          while heights[l] > heights[l+i]:
              s += heights[l] - heights[l+i]
              i += 1
          l += i
      else:
          while heights[r] > heights[r-i]:
              s += heights[r] - heights[r-i]
              i += 1
          r -= i
  return s

def main():
  print(trap([1,3,2,4,1,3,1,4,5,2,2,1,4,2,2]))
  print(trap([0,1,2,0,3,0,1,2,0,0,4,2,1,2,5,0,1,2,0,2]))
  print(trap([4,2,0,3,2,4,3,4]))
  print(trap([9,6,8,8,5,6,3]))
  print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))

main()