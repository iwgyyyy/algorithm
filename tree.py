# -*-coding:utf-8-*-
class Node(object):

    def __init__(self,value):
        self.val = value
        self.lchild = None
        self.rchild = None


class Tree(object):

    def __init__(self):
        self.root=None

    def add(self,val):
        '''add val to the Tree'''
        node=Node(val)
        if not self.root:
            self.root=node
            return
        queue=[self.root]
        while queue:
            cur_node=queue.pop(0)
            if not cur_node.lchild:
                cur_node.lchild=node
                return
            else:
                queue.append(cur_node.lchild)
            if not cur_node.rchild:
                cur_node.rchild=node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        '''广度遍历'''
        if not self.root:
            return
        queue=[self.root]
        while queue:
            cur_node=queue.pop(0)
            print(cur_node.val,end=' ')
            if cur_node.lchild:
                queue.append(cur_node.lchild)
            if cur_node.rchild:
                queue.append(cur_node.rchild)

    def preorder(self,node):
        '''前序遍历递归做法'''
        if not node:return
        print(node.val,end=' ')
        self.preorder(node.lchild)
        self.preorder(node.rchild)
        '''前序遍历迭代做法'''
        '''if not node:return 
        stack,res=[root],[]
        while stack:
            cur_node=stack.pop()
            res.append(cur_node.val)#表示该节点的值
            if cur_node.right:queue.append(cur_node.right)
            if cur_node.left:queue.append(cur_node.left)
        return res'''

    def inorder(self,node):
        '''中序遍历'''
        if not node: return
        self.inorder(node.lchild)
        print(node.val,end=' ')
        self.inorder(node.rchild)

    def postorder(self,node):
        '''后序遍历'''
        if not node: return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.val,end=' ')

if __name__=='__main__':
    tree=Tree()
    for i in range(10):
        tree.add(i)


