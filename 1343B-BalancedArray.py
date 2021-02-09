import sys
n = int(sys.stdin.readline().strip())
list1 = []

i = 0

while i < n:
    list1.append(int(sys.stdin.readline().strip()))
    i=i+1
lst3=[]
for var in list1:
    j=0
    if var%4==0:
        lst1=[]
        lst2=[]
        for j in range(0,var//2):
            lst1.append(int(2*j+2))
        for j in range(0, var//2):
            lst2.append(int(2*j+1))
        sum1=sum(lst1)
        sum2=sum(lst2)
        var1 = len(lst2)-1
        diff=abs(sum1-sum2)+lst2[var1]

        lst2[var1]=diff
        lst3.append('YES')

        lst3.append(' '.join(map(str,lst1+lst2)))
    else:
        lst3.append('NO')
for m in lst3:
    print(m)





