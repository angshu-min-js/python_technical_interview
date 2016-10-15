class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_bst(self.root, new_val)

    def search(self, find_val):
        return self.search_bst(self.root, find_val)

    def insert_bst(self, current, new_val):
        if current.value<new_val:
            if current.right:
                self.insert_bst(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_bst(current.left, new_val)
            else:
                current.left = Node(new_val)

    def search_bst(self, current, find_val):
        if current:
            if current.value == find_val:
                return current.value
            elif current.value < find_val:
                return self.search_bst(current.right, find_val)
            else:
                return self.search_bst(current.left, find_val)
        else:
            return False

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))
print ("Root", tree.root.value)
print ("Right", tree.root.right.value)
print ("Left", tree.root.left.value)

'''
        4
        |
       / \
      2   5
     / \
    1   3
'''
