import sys

t = int(sys.stdin.readline().rstrip())
numl=[]
while t > 0:
    numl.append(int(sys.stdin.readline().rstrip()))
    t = t - 1
for i in numl:
    if i % 2 == 0:
        var1 = i // 2
        print(str(var1) + ' ' + str(var1))
    else:
        var1=i
        print('1' + ' ' + str(var1-1))