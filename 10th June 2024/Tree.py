class Node:
    def __init__(self,u):
        self.data=u
        self.right=None
        self.left=None
class Tree:
    def __init__(self):
        self.root=None
    def create(self,root,x):
        if self.root==None:
            self.root=Node(x)
        elif (self.root.data>x):
            self.create(root.left,x)
        else:
            self.create(root.right,x)
t1=Tree()
t1.create(t1.root,10)
t1.create(t1.root,3)
t1.create(t1.root,16)
