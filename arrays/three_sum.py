from typing import List

def threeSum(nums: List[int]):
  nums.sort()
  results = []
  for x in range(len(nums)):
    target = nums[x]
    if x > 0 and nums[x] == nums[x-1]:
      continue

    l, r = x+1, len(nums)-1
    while l < r:
      threeSum = nums[l] + nums[r] + target
      if threeSum == 0:
        results.append([target, nums[l], nums[r]])
        l += 1
        while nums[l] == nums[l-1] and l < r:
          l += 1
      elif threeSum > 0:
        r-= 1
      else:
        l += 1
  return results

def main():
  print(threeSum([-1, 0, 1, 2, -1, -4]))
main()