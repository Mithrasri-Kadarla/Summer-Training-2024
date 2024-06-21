class Node:
    def __init__(self, u):
        self.data = u
        self.right = None
        self.left = None

class Tree:
    def __init__(self):
        self.root = None

    def create(self, root, x):
        if root is None:
            return Node(x)
        if x < root.data:
            root.left = self.create(root.left, x)
        else:
            root.right = self.create(root.right, x)
        return root

    def insert(self, x):
        if self.root is None:
            self.root = Node(x)
        else:
            self.create(self.root, x)

    def preorder(self, root):
        if root:
            print(root.data, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=' ')

t1 = Tree()
t1.insert(10)
t1.insert(3)
t1.insert(16)
t1.insert(1)
t1.insert(5)

print("Preorder traversal:")
t1.preorder(t1.root)
print("\nInorder traversal:")
t1.inorder(t1.root)
print("\nPostorder traversal:")
t1.postorder(t1.root)
