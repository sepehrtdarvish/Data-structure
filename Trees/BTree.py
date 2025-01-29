class Node:
    def __init__(self, leaf=False):
        self.keys = []
        self.childern = []
        self.leaf = leaf

class BTree():
    def __init__(self, t):
        self.root = Node(leaf=True)
        self.t = t

    def search(self, value, node=None):
        node = self.root if node == None else node

        i = 0
        if node.leaf == True:
            return False
        
        while value > node.keys[i] and i < len(node.keys):
            i += 1

        if node.keys[i] == value:
            return True
        
        else:
            return self.search(value=value)
