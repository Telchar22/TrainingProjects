from collections import defaultdict

def a(n):
    d = defaultdict(list)
    ans = []
    for i,j in enumerate(groupSizes):
        d[j].append(i)
        if j == len(d[j]):
            #ans.append(d[j][:])
            ans.append(d.pop(j))
            d[j].clear()
    return ans

groupSizes = [3,3,3,3,3,1,3]
a = a(groupSizes)
print(a)
