#You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

#Return true if you can reach the last index, or false otherwise.

#O(n^2)
def jump_game_brute(nums):
  num_len = len(nums)
  dp = [False] * num_len
  dp[0] = True
  for i in range(num_len):
    if dp[i]:
      if nums[i] == 0:
        continue
      for x in range(nums[i]):
        if i+x+1 < num_len:
          dp[i+x+1] = True
          if i + x +1 == num_len-1:
            return True
  return dp[num_len-1]

#O(n), start from the end and be greedy
def jump_game_greedy(nums):
  n = len(nums)
  goal = n-1
  for i in range(n-1, -1, -1):
    if nums[i] + i >= goal:
      goal = i
  return goal == 0

def main():

  print(jump_game_brute([2,3,1,1,4]))
  print(jump_game_brute([3,2,1,0,4]))

  print(jump_game_greedy([2,3,1,1,4]))
  print(jump_game_greedy([3,2,1,0,4]))

main()