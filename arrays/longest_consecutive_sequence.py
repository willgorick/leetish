# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

from typing import List

def longestConsecutive(nums: List[int]) -> int:
  s = set()
  ans = 0
  
  for elem in nums:
    s.add(elem)
      
  for i in range(len(nums)):
    #if this number is the start of a new sequence
    if nums[i]-1 not in s:
      j = nums[i]
      while (j in s):
        j+=1 
          
      ans = max(ans, j-nums[i])
  return ans

def main():
  print(longestConsecutive([100,4,200,1,3,2]))
  print(longestConsecutive([8,7,5,4,1,2,10,9,3]))

main()