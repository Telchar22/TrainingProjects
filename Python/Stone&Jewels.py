class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        a = set(J)
        b = list(S)
        counter = 0
        for i in b:
            if i in a:
                counter+=1
        return counter
J = 'aAcd'
S = 'aAAAbbbbbcd'
p = Solution()
print(p.numJewelsInStones(J,S))

# Method 2
from collections import Counter
ctr = 0
temp = Counter(S)
for i in J:
    ctr += temp[i]
print(ctr)
