class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root=None
    
    def create(self,root,x):
        if root is None:
            return Node(x)
        elif x<root.data:
            root.left=self.create(root.left,x)
        else:
            root.right=self.create(root.right,x)
        return root
    
    def insert(self,x):
        if self.root is None:
            self.root=Node(x)
        else:
            self.create(self.root,x)

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)
    
    def preorder(self,root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")
            
    def add(self,root):
        if root: return root.data+self.add(root.left)+self.add(root.right)
        else: return 0

    # def even_odd_sum(self, root):
    #     if root is None:
    #         return 0,0
    #     el,ol=self.even_odd_sum(root.left)
    #     er,o_r=self.even_odd_sum(root.right)
    #     if root.data%2==0:
    #         return el+er+root.data,ol+o_r
    #     else:
    #         return el+er,ol+o_r+root.data

    def even(self, root):
        if root is None:
            return 0
        ev=0
        if root.data%2==0:
            ev+=root.data
        ev+=self.even(root.left)
        ev+=self.even(root.right)
        return ev
    
    
    def odd(self, root):
        if root is None:
            return 0
        odd=0
        if root.data%2!=0:
            odd+=root.data
        odd+=self.odd(root.left)
        odd+=self.odd(root.right)
        return odd

    # def diff(self, root):
    #     es=self.even(root)
    #     os=self.odd(root)
    #     return es-os

    # def diff(self, root):
    #     if root is None:
    #         return 0
    #     ev,odd =0,0
    #     stack=[root]
    #     while stack:
    #         curr=stack.pop()
    #         if curr.data%2==0:
    #             ev+=curr.data
    #         else:
    #             odd+=curr.data
    #         if curr.right:
    #             stack.append(curr.right)
    #         if curr.left:
    #             stack.append(curr.left)

    #     return ev-odd

    def diff(self,root):
        if root is None:
            return 0
        s=0
        if root.data%2==0:
            s+=root.data+self.diff(root.left)+self.diff(root.right)
        else:
            s-=root.data-self.diff(root.left)-self.diff(root.right)
        return s

    def height(self, root):
        if root is None:
            return -1
        else:
            lh=self.height(root.left)
            rh=self.height(root.right)
            return max(lh,rh)+1
           #heihgt of none if -1 

    def is_balanced(self,root):
        return abs(self.height(root.left)-self.height(root.right))<=1

    
    def leaf_nodes(self,root):
        if root.left is None and root.right is None:
            return 1
        return self.leaf_nodes(root.left)+self.leaf_nodes(root.right)


    def leaf_nodes_sum_print(self,root):
        if root.left is None and root.right is None:
            return root.data
        return self.leaf_nodes_sum_print(root.left)+self.leaf_nodes_sum_print(root.right)

    def search_node(self,root,n,d):
        if root is None:
            return None,0
        if root.data==n:
            return root.data,d
        if n<root.data:
            return self.search_node(root.left,n,d+1)
        else:
            return self.search_node(root.right,n,d+1)

        
tree=Tree()
tree.insert(10)
tree.insert(5)
tree.insert(20)
tree.insert(1)
tree.insert(7)
tree.insert(6)
tree.insert(8)

tree.inorder(tree.root)
print()
tree.preorder(tree.root)
print()
tree.postorder(tree.root)
print()
print(tree.add(tree.root))



print("Even sum:",tree.even(tree.root))
print("odd sum:",tree.odd(tree.root))
print("Even odd diff:",tree.diff(tree.root))

print("Height:",tree.height(tree.root))

if tree.is_balanced(tree.root):
    print("Balanced")
else:
    print("Not Balanced")

print("Leaf Nodes :",tree.leaf_nodes(tree.root))
print("Leaf Nodes sum Printing:",tree.leaf_nodes_sum_print(tree.root))
print("The deapth of searched element is :",tree.search_node(tree.root,6,0))
