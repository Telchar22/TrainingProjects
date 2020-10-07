from typing import List
def findNumbers(nums: List[int]) -> int:
    ctr = 0
    for i in nums:
        if (len(str(i))%2) == 0:
            ctr+=1
    return ctr

nums = [15,2,3,444,5,65,7,8555]
print(findNumbers(nums))
