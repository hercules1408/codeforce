import sys

t = int(sys.stdin.readline().rstrip())
out=[]
while t > 0 :
    n = int(sys.stdin.readline().rstrip())

    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))

    var=len(set(arr))
    out.append(var)
    t=t-1
for var2 in out:
    print(var2)




