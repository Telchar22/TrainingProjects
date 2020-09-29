from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        dictionary = tuple(zip(nums[0:n], nums[n:2*n]))
        nums = [i for t in dictionary for i in t]
        return nums

nums = [1,1,2,2]
n= 2
p = Solution()
print(p.shuffle(nums,n))
