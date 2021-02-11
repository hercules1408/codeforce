import sys

n = int(sys.stdin.readline().strip())

list1 = list(map(int, sys.stdin.readline().strip().split()))

outlst = []
lst1 = []
lstval = []
outlst1 = []
whl=1
while whl <= n//2:
    #print('test')


    for i in range(len(list1)):
        if len(lst1) == 3:
            outlst.append(lst1)
            #print(outlst)
            lst1 = []
            lstval = []
        if list1[i] == 1:
            #print('lst1')
            if list1[i] not in lstval and i not in outlst1 :
                #print('issue', lst1, list1[i])
                lst1.append(i)
                outlst1.append(i)
                lstval.append(list1[i])

        elif list1[i] == 2 :
            #print('issue2', lst1, list1[i])
            if list1[i] not in lstval and i not in outlst1:
                lst1.append(i)
                outlst1.append(i)
                lstval.append(list1[i])
        elif list1[i] == 3:
            #print('issue3', lst1, list1[i])
            if list1[i] not in lstval and i not in outlst1:
                lst1.append(i)
                outlst1.append(i)
                lstval.append(list1[i])
        #print(outlst1,lst1,whl)
    if len(lst1) == 3:
        outlst.append(lst1)
        # print(outlst)
        lst1 = []
        lstval = []
    whl = whl+1
#print(outlst1,lst1,whl)
lenout=len(outlst)
print(lenout)
if lenout>0:
    for out in outlst:
        for out1 in out:
            print(out1+1,end=' ')
        print()

