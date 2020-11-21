from random import randrange

def merge_sort(li):
    l=len(li)
    if l<2:return li
    #拆分列表
    mid=l//2
    #left_li为归并排序后的新的有序列表
    left_li=merge_sort(li[:mid])
    #right_li为归并排序后的新的有序列表
    right_li=merge_sort(li[mid:])


    #合并两个有序列表 l_cur为左列表的指针，r_cur为右列表的指针
    l_cur=r_cur=0
    #res为合并后的两个有序列表
    res=[]
    #left_len right_len分别为左右列表的长度
    left_len,right_len=len(left_li),len(right_li)
    #合并
    while l_cur<left_len and r_cur<right_len:
        if left_li[l_cur]<=right_li[r_cur]:
            res.append(left_li[l_cur])
            l_cur+=1
        else:
            res.append(right_li[r_cur])
            r_cur+=1
    #将两个有序列表剩下的元素添加到res中
    '''剩下的元素一定比res中的元素都大，因为最后一次比较后较小的元素被
    添加到res中，剩下的元素一定比最后一个添加的元素大，即比res中所有元素都大'''
    res+=left_li[l_cur:]
    res+=right_li[r_cur:]
    return res

if __name__=='__main__':
    li=[]
    for i in range(20):
        li.append(randrange(100))
    print('原数组:',li)
    print('排序后的数组为:',merge_sort(li))
