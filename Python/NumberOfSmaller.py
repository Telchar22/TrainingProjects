from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = {}
        for i, j in enumerate(sorted(nums)):
            if j not in d:
                d[j] = i
        nums = [d[n] for n in nums]
        return nums
nums = [8,1,2,2]
p = Solution()
print(p.smallerNumbersThanCurrent(nums))
