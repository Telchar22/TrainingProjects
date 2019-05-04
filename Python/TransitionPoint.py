def transitionPoint(arr, n):              #returning position of 0 to 1 change
    for i in range(n):
        if(arr[i]==0 and arr[i+1]==1):
            return(i+1)



if __name__=='__main__':
    a=int(input())
    for i in range(a):
       n=int(input())

       arr=list(map(int,input().split()))
    print(transitionPoint(arr, n))
