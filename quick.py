from random import *
x=[]
for i in range(30):
    x.append(randrange(100))
print('原数组:',x)

def quick(mylist):
    #如果列表长度小于2，则不用排序
    if len(mylist)<2:
        return mylist
    #定义一个中间值
    mid_value=mylist[0]
    #该列表中比中间值小的元素组成一个列表
    left_list=[i for i in mylist[1:] if i <=mid_value]
    #比中间值大的元素组成一个列表
    right_list=[i for i in mylist[1:] if i>mid_value]
    #返回值为递归，即返回经过快排的左列表+中间值+经过快排的右列表
    return quick(left_list)+[mid_value]+quick(right_list)

print('快速排序后数组:',quick(x))
