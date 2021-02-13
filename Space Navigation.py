import sys

t = int(sys.stdin.readline().rstrip())
while t > 0:
    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    arrstr = sys.stdin.readline().rstrip()
    x = 0
    y = 0
    dirlist = [0] * 4
    xf = 0
    yf = 0
    for i in arrstr:

        if i == 'U':
            dirlist[0] = dirlist[0] + 1
        elif i == 'D':
            dirlist[1] = dirlist[1] + 1
        elif i == 'R':
            dirlist[2] = dirlist[2] + 1
        elif i == 'L':
            dirlist[3] = dirlist[3] + 1
    if ((arr[0] <= 0 and dirlist[3] >= abs(arr[0])) or (arr[0] >= 0 and dirlist[2] >= abs(arr[0]))) and ((arr[1] >= 0 and dirlist[0] >= abs(arr[1])) or (arr[1] <= 0 and dirlist[1] >= abs(arr[1]))):
        print('YES')
    else:
        print('NO')

    t = t - 1
