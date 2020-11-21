from random import *
x=[]
for i in range(10):
    x.append(randrange(10))
print('原序列为:',x)
i,l=0,len(x)
while i<l:
    mymin=x[i]
    for a in range(i,l):
        mymin=min(mymin,x[a])
        if mymin==x[a]:j=a
    if mymin==x[j]:
        x[i],x[j]=x[j],x[i]
    i+=1
print('选择排序后序列为:',x)
