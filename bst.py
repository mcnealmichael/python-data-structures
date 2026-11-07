class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        # planting the very first node
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root

        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node # plant the node here
                    return
                current = current.left # keep walking down the left side
            elif value > current.value:
                if current.right is None:
                    current.right = new_node # plant the node here
                    return
                current = current.right # keep walking down the right side
            else:
                return

    def search(self, value):
        current = self.root

        while current is not None:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        raise Exception(f"ERROR: {value} not found")

    def minimum(self):
        current = self.root

        while current.left is not None:
            current = current.left
        return current.value

    def maximum(self):
        current = self.root

        while current.right is not None:
            current = current.right
        return current.value

    def _inorder(self, node):
        if node is None:
            return []
        left_done = self._inorder(node.left)
        right_done = self._inorder(node.right)
        return left_done + [node.value] + right_done

    def inorder(self):
        return self._inorder(self.root)

    def delete(self, value):
        current = self.root
        parent = None

        while current is not None:
            if value == current.value:
                break
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right
        if current is None:
            raise Exception(f"ERROR: {value} not found")

        if current.left is None and current.right is None:
            repla

        if parent is None:
            self.root = None
        elif parent.left is current:
            parent.left = None
        else:
            parent.right = None

# t = BinarySearchTree()
# t.insert(30)
# t.insert(70)
# t.insert(20)
# t.insert(40)

# # 1 - structure, reading the pointers directly
# print(t.root.value)                 # expect 30
# print(t.root.right.value)           # expect 70
# print(t.root.left.value)            # expect 20
# print(t.root.right.left.value)      # expect 40

# # 2 - search hits
# print(t.search(40).value)           # expect 40

# # 3 - search miss: the contract in action
# try:
#     t.search(99)
# except Exception as e:
#     print("caught: ", e)            # expect the not-found error

# # 4 - duplicate insert: predict, then confirm the tree is unchanged
# t.insert(30)
# print(t.root.value)                 # expect 30
# print(t.root.right.value)           # expect 70

# a = BinarySearchTree()
# for v in [30, 70, 20, 40, 10, 80]:
#     a.insert(v)
# print(a.minimum())                  # expect 10
# print(a.maximum())                  # expect 80

# b = BinarySearchTree()
# b.insert(30)
# print(b.minimum())                  # expect 30
# print(b.maximum())                  # expect 30

# c = BinarySearchTree()
# for v in [30, 40, 50]:
#     c.insert(v)
# print(c.minimum())                  # expect 30 - the root itself is the minimum

# d = BinarySearchTree()
# for v in [30, 70, 20, 40, 10, 80]:
#     d.insert(v)
# print(d.inorder())                  # expect [10, 20, 30, 40, 70, 80]

# e = BinarySearchTree()
# e.insert(30)
# print(e.inorder())                  # expect [30]

# f = BinarySearchTree()
# print(f.inorder())                  # expect [] - base case at the very top

# g = BinarySearchTree()
# for v in [10, 20, 30, 40, 70, 80]:  # expect [20, 30, 40, 70, 80]
#     g.insert(v)
# g.delete(10)
# print(g.inorder())

t = BinarySearchTree()
for v in [30, 70, 20, 40, 10, 80]:
    t.insert(v)
t.delete(10)
print(t.inorder())   # expect [20, 30, 40, 70, 80]
t.delete(80)
print(t.inorder())   # expect [20, 30, 40, 70]

u = BinarySearchTree()
u.insert(30)
u.delete(30)
print(u.inorder())   # expect []

t.delete(99)         # expect ERROR: 99 not found
