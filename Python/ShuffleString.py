from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        tmp = list(s)
        dictionary = {}
        dictionary = dict(zip(indices, tmp))
        s = list(dict(sorted((indices, tmp) for (indices,tmp) in dictionary.items())).values())
        s = "".join(s)
        return s


s = "sdfgdfgg"
indices = [4,5,6,7,0,2,1,3]
p = Solution()
print(p.restoreString(s, indices))