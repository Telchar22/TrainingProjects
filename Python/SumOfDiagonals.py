
def printDiagonalSums(mat, n):
    ans = 0
    n = len(mat)
    for i in range(0,n):
        if i == n - i - 1:
            ans -= mat[i][n - i - 1]
        ans += mat[i][i] + mat[i][n - i - 1]
    print(f"Diag:{ans}")



k = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [1, 2, 3, 4],
     [5, 6, 7, 8]]

an = [[1,2,3],
       [4,5,6],
       [7,8,9]]

a = [[1,1,1,1],
     [1,1,1,1],
     [1,1,1,1],
     [1,1,1,1]]

for i in [k, an,a]:
    printDiagonalSums(i, len(i))