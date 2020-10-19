S = "(()())(())"
l = r = j = 0
res = []
for i in range(len(S)):
    if S[i] == '(':
        l+=1
    if S[i] == ')':
        r+=1
    if l == r:
        res.append(S[j + 1: i])
        j = i + 1
print(''.join(res))
