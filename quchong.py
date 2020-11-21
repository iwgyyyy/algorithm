from random import randrange
a=[randrange(10) for j in range(20)]
print('去重前列表为:{}'.format(a))
k=0
for i in range(len(a)):
    j=0
    while j<k and a[i]!=a[j]:
        j+=1
    if j==k:
        if k!=i:a[k]=a[i]
        k+=1
a=a[:k]
print('去重后列表为:{}'.format(a))
