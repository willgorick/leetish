#same as jump game, but goal is to find the minimum number of jumps needed to reach the final index

#another greedy algo!
def jump_game_2(nums):
  result = 0
  l = r = 0
  while r < len(nums)-1:
    farthest = 0
    for i in range(l, r+1):
      farthest = max(farthest, i+nums[i])
    l = r+1
    r = farthest
    result += 1
  return result
 
def main():
  print(jump_game_2([2,3,1,1,4]))

main()