class Solution:
    def decomp(self, nums: List[int]) -> List[int]:
        d = []
        for i in range(len(nums)//2):
            freq = nums[2*i]
            val = nums[2*i +1]
            tmp = [val]*freq
            d += tmp
        return d
nums = [1,2,3,4]       
p = Solution()
print(p.decomp(nums))
