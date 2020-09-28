from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        nums = [sum(nums[0:i+1]) for i in range(len(nums))]
        return nums

nums = [1, 2, 3, 4, 5, 6]
print(nums)

s = Solution()
print(s.runningSum(nums))
