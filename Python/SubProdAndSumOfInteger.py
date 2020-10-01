class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        n = list(map(int, n))
        p = n[0]
        s = n[0]
        for i in range(1, len(n)):
            p = p*n[i]
        
        for j in range(1, len(n)):
            s = s + n[j]
            
        return (p-s)
