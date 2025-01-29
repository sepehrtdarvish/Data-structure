class Node():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.height = 1

    def get_height(self):
        return self.height if self else 0
    
    def update_height(self):
        left_height = self.left.get_height() if self.left else 0
        right_height = self.right.get_height() if self.right else 0
        self.height = 1 + max(left_height, right_height)

    def get_balance(self):
        left_height = self.left.get_height() if self.left else 0
        right_height = self.right.get_height() if self.right else 0
        return left_height - right_height
    
class BSTree():
    def __init__(self):
        self.root = None

    def search(self, value):
        return self._recursive_search(node=self.root, value=value)

    def _recursive_search(self, node, value):
        if node.value == value:
            return True
        
        elif value > node.value:
            if node.right:
                return self._recursive_search(node.right, value)
            else:
                return False

        else:
            if node.left:
                return self._recursive_search(node.left, value)
            else:
                return False
            

    def right_rotate(self, node):
        x = node.left
        y = x.right

        x.right = node
        node.left = y

        node.update_height()
        x.update_height()

        return x

    def left_rotate(self, node):
        x = node.right
        y = x.left

        x.left = node
        node.right = y

        node.update_height()
        x.update_height()

        return x

    def insert(self, value):
        return self._recursive_insert(node=self.root, value=value)
    

    def _recursive_insert(self, node, value):
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._recursive_insert(node=node.left, value=value)
        else:
            node.right = self._recursive_insert(node=node.right, value=value)

        # Update height of current node
        node.update_height()

        node.height = 1 + max(node.left.get_height())
        balance = node.get_balance()


        if balance > 1 and value < node.left.value:
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and value > node.right.value:
            return self.left_rotate(node)

        # Left Right Case
        if balance > 1 and value > node.left.value:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case
        if balance < -1 and value < node.right.value:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

tree = BSTree()
tree.insert(20)
tree.insert(10)
tree.insert(30)
tree.insert(25)