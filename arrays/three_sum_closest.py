from typing import List


class Solution:
  def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    bestSum = sum(nums[:3])
    for i in range(len(nums)-2):
      l, r = i+1, len(nums)-1
      while l < r:
        threeSum = nums[i] + nums[l] + nums[r]
        if abs(threeSum - target) < abs(bestSum - target):
          bestSum = threeSum
        if threeSum == target:
            return threeSum
        if threeSum > target:
            r -= 1
        else:
            l += 1
    return bestSum

def main():
  solution = Solution()
  print(solution.threeSumClosest([-1,2,1,-4], 1))

main()
