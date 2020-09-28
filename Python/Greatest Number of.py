from typing import List

class Solution:
    def isGreatestNumberPossible(items: List[int], extras: int) -> List[bool]:
        ans = [True if(items[i]+extras >= max(items)) else False for i in range(len(items))]
        return ans


items = [2, 3, 5, 1, 3]
extras = 3
print(Solution.isGreatestNumberPossible(items, extras))