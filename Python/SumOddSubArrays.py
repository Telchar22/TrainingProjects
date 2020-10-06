from typing import List
class Solution2:
    def sumOddLengthSubarrays2(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        for i, j in enumerate(arr):
            ans += ((i + 1) * (n - i) + 1) // 2 * j
        return ans

arr = [1,4,2,5,3]
p2 = Solution2()
print(p2.sumOddLengthSubarrays2(arr))
