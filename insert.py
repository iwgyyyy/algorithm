from random import randrange

a=[randrange(100) for i in range(20)]
print('排序前的列表:',a)

def bisect(num,k):
    fir,sec=0,len(num)-1
    while fir<=sec:
        mid=(fir+sec)//2
        if num[mid]<=k:fir=mid+1
        else:sec=mid-1
    return fir

for i in range(1,len(a)):
    x=a.pop(i)
    temp=bisect(a[:i],x)
    a[temp:temp]=[x]

print('排序后的列表为:',a)

