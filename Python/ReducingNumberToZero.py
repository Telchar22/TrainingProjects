class Solution:
    def numberOfSteps (self, num: int) -> int:
        ctr = 0
        while True:
            if num == 0:
                break
            if num%2==0:
                num = num/2
            else:
                num = num - 1
            ctr += 1
        return ctr


num = 14
p = Solution()
print(p.numberOfSteps(num))