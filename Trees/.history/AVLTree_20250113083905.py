class Node():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class AVLTree():
    def __init__(self):
        self.root = None

    def search(self, value):
        return self._recursive_search(self.root, value)

    def _recursive_search(self, node, value):
        if value >= node.value:
            if node.right:
                return self._recursive_search(node.right, value)
            else:
                return False
        else:
            if node.left:
                return self._recursive_search(node.left, value)
            else:
                return False
            
node = Node(20)
tree = AVLTree()
tree.root = node
node.right = Node(30)
node.left = Node(10)
print(tree.search(10))