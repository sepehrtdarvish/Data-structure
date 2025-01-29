class Node():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BSTree():
    def __init__(self):
        self.root = None

    def search(self, value):
        return self._recursive_search(node=self.root, value=value)

    def _recursive_search(self, node, value):
        if node.value == value:
            return True
        
        elif value >= node.value:
            if node.right:
                return self._recursive_search(node.right, value)
            else:
                return False

        else:
            if node.left:
                return self._recursive_search(node.left, value)
            else:
                return False
            

    def add(self, value):
        return self._recursive_add(node=self.root, value=value)
    
    def _recursive_add(self, node, value):
        if value >= node.value:
            if node.right:
                return self._recursive_add(node=node.right, value=value)
            else:
                node.right = Node(value=value)
        else:
            if node.left:
                return self._recursive_add(node=node.left, value=value)
            else:
                node.left = Node(value=value)
    
    @staticmethod
    def _height(node, direction):
        count = 1
        queue = [node.direction]
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