from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = []
        greaterThan2 = []

        def kSum(target: int, k: int, start: int):
            if k > 2:
                for i in range(start, len(nums)-k+1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    greaterThan2.append(nums[i])
                    kSum(target-nums[i], k-1, i+1)
                    greaterThan2.pop()
                return
            elif k == 2:
                # base case, basically two sum II
                l, r = start, len(nums)-1
                while l < r:
                    twoSum = nums[l] + nums[r]
                    if twoSum == target:
                        result = []
                        for num in greaterThan2:
                            result.append(num)
                        result.append(nums[l])
                        result.append(nums[r])
                        results.append(result)
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif twoSum < target:
                        l += 1
                    else:
                        r -= 1
        kSum(target, 4, 0)
        return results

def main():
  solution = Solution()
  print(solution.fourSum([-1,2,1,-4,8], 7))

main()
