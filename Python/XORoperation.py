class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        bit = 0
        for i in range(n):
            bit = bit ^ (start + 2*i)
        return bit
 p = Solution()
 n = 5
 start = 7
 print(p.xorOperation(n, start))
