import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))


start=arr[0]
worst=arr[0]
sum=0
for i in range(1,len(arr)):

    if arr[i]>start:

        sum=sum+1
        start=arr[i]
        #print(start)

    elif arr[i]<worst:
        sum = sum + 1
        worst = arr[i]
        #print(worst)

print(sum)