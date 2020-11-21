class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
    def __repr__(self):
        return '<ListNode val={},next={}>'.format(self.val,self.next)

class Sort_of_ListNode:
    '''返回一个升序链表'''
    def insert_sort(self,head:ListNode) -> ListNode:
        '''插入排序排序链表'''
        if not head or not head.next:return head
        root=ListNode(next=head)
        while head.next:
            #如果链表的后一个节点值大于或等于当前节点值，则指针向后移
            if head.next.val>=head.val:
                head=head.next
                continue
            pre=root#定义一个指针指向头节点
            '''从头节点开始向后循环，此时head.next节点表示需要往前插入的节点，即比head节点的val值大'''
            while pre.next.val<head.next.val:
                pre=pre.next
            temp=head.next
            head.next=temp.next
            temp.next=pre.next
            pre.next=temp
        return root.next

    def merge_sort(self,head:ListNode) -> ListNode:
        '''归并排序排序链表'''
        if not head or not head.next:return head
        #定义快慢指针，快指针每次跳两个，慢指针每次走一个，即可找到中点
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        #将链表从中点处切开
        mid, slow.next = slow.next, None
        #递归定义left为左链表，right为右链表
        left, right = self.merge_sort(head), self.merge_sort(mid)
        #定义res为头节点，h指针指向res
        h = res = ListNode(0)
        #合并链表
        while left and right:
            #若左链表值小于右链表，则将左链表节点连接到res上，且left向后移动一位
            if left.val < right.val: 
                h.next, left = left, left.next 
            #反之，将右链表节点添加到res上，right向后移动一位
            else: 
                h.next, right = right, right.next
            h = h.next
        #和归并排序一样，若左链表或右链表还有剩余的值，则直接连接到res上
        h.next = left if left else right
        return res.next

    def choice_sort(self,head:ListNode) -> ListNode:
        '''选择排序排序链表'''
        if not head or not head.next:return head
        temp=head
        min_node,min_val=temp,temp.val
        #每次循环一遍链表，找到其最小值，插入第一个节点
        #第二遍循环链表，其最小值插入第二个节点，以此类推
        while temp.next:
            min_val=min(temp.next.val,min_val)
            if min_val==temp.next.val:
                cur=temp
                min_node=temp.next
            temp=temp.next
        #递归的方式插入节点
        if min_node==head:
            min_node.next=self.choice_sort(head.next)
        else:
            cur.next=min_node.next
            min_node.next=self.choice_sort(head)
        return min_node

    def repr_ListNode(self,head:ListNode):
        '''格式化输出链表'''
        x=[]
        while head:
            x.append(head.val)
            head=head.next
        return x
if __name__=='__main__':
    a=[ListNode(10-i) for i in range(10)]
    '''此时a列表存储的是10个链表，其中a[0]是10—>9...->0,a[8]是9->8..->0,a[9]是0
    当使用了插入排序后,a[0]变为10，a[9]变成了0->1->2..->10'''
    for i in range(len(a)-1):
        a[i].next=a[i+1]
    x=Sort_of_ListNode()
    print('排序前链表为:',x.repr_ListNode(a[0]))
    #print('插入排序排序链表:',x.repr_ListNode(x.insert_sort(a[0])))
    #print('选择排序排序链表:',x.repr_ListNode(x.choice_sort(a[0])))
    print('归并排序排序链表:',x.repr_ListNode(x.merge_sort(a[0])))
