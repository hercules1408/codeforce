import sys
n = int(sys.stdin.readline().strip())
list1 = []

i = 0

while i < n:
    list1.append(int(sys.stdin.readline().strip()))
    i=i+1

for var in list1:
    j=1
    while j<=var:
        print('1',end=' ')

        j=+j+1
    print()



