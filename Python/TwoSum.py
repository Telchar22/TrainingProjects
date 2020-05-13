# Finding indexes of 2 elements that sum gives target number
def TwoSum(num, target):
    d = {}
    for i in range(len(num)):
        n = target - num[i]
        if n in d:
            print([d[n], i])
        else:
            d[num[i]] = i  # after 1st iter if num[0] = 5, we get {5 : 0}


if __name__ == "__main__":
    L = [int(x) for x in input().split()]
    T = int(input())
    TwoSum(L, T)
