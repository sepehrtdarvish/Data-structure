class Node():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.height = 1

    def get_height(self):
        return self.height

    def get_balance(self):
        return self.left.get_height() - self.right.get_height()

    
class BSTree():
    def __init__(self):
        self.root = None

    def search(self, value):
        return self._recursive_search(node=self.root, value=value)


    def right_rotate(self, node):
        x = node.left
        y = x.right

        x.right = node
        node.left = y

        node.height = 1 + max(node.left.get_height(), node.right.get_height())
        x.height = 1 + max(x.left.get_height(), x.right.get_height())

        return x

    def left_rotate(self, node):
        x = node.right
        y = x.left

        x.left = node
        node.right = y

        node.height = 1 + max(node.left.get_height(), node.right.get_height())
        node.height = 1 + max(x.left.get_height(), x.right.get_height())



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
            

    def insert(self, value):
        return self._recursive_insert(node=self.root, value=value)
    
    def _recursive_insert(self, node, value):
        if value > node.value:
            if node.right:
                return self._recursive_insert(node=node.right, value=value)
            else:
                node.right = Node(value=value)
        else:
            if node.left:
                return self._recursive_insert(node=node.left, value=value)
            else:
                node.left = Node(value=value)
    
    @staticmethod
    def _height(node):
        count = 1
        queue = [node]
        while queue:
            current = queue.pop(0)
            if current.right:
                count += 1
                queue.append(current.right)
            if current.left:
                count += 1
                queue.append(current.left)


    
node = Node(20)
tree = BSTree()
tree.root = node
node.right = Node(30)
node.left = Node(10)
print(tree.search(10))