import sys
n = int(sys.stdin.readline().strip())
i=0
arr=[]
while i<n:
    arr.append(int(sys.stdin.readline().rstrip()))
    i=i+1

outall=[]
for var in arr:
    out=[]
    out.append(var)
    for j in range(var-1):
        out.append(j+1)

    outall.append(out)
for var3 in outall:
    print(*var3,sep=' ')



