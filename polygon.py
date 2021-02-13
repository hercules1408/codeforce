import sys

t = int(sys.stdin.readline().rstrip())

while t>0:
    inp=int(sys.stdin.readline().strip())

    if inp%4==0:
        print('YES')
    else:
        print('NO')
    t=t-1
