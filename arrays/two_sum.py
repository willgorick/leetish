from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
  complements = {}
  for i in range(len(nums)):
    if nums[i] in complements:
      return [complements[nums[i]], i]
    else:
      complements[target - nums[i]] = i