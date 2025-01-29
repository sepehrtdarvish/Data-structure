class Node:
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


class BSTree:
    def __init__(self):
        self.root = None

    def search(self, value):
        return self._recursive_search(node=self.root, value=value)

    def _recursive_search(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        elif value > node.value:
            return self._recursive_search(node.right, value)
        else:
            return self._recursive_search(node.left, value)

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
        # Assign the returned new root back to self.root
        self.root = self._recursive_insert(node=self.root, value=value)

    def _recursive_insert(self, node, value):
        # Perform standard BST insertion
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._recursive_insert(node=node.left, value=value)
        else:
            node.right = self._recursive_insert(node=node.right, value=value)

        # Update height of the current node
        node.update_height()

        # Get balance factor to check if unbalanced
        balance = node.get_balance()

        # Balance the tree
        # Left Left Case
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

        return node


if __name__ == "__main__":
    tree = AVLTree()
    tree.insert_value(10)
    tree.insert_value(20)
    tree.insert_value(30)
    tree.insert_value(40)
    tree.insert_value(50)

    print("Tree after insertion:")
    # In-order traversal to print the tree
    def inorder_traversal(root):
        if root:
            inorder_traversal(root.left)
            print(root.value),
            inorder_traversal(root.right)

    inorder_traversal(tree.root)
    print()

    tree.delete_value(20)
    print("Tree after deletion of 20:")
    inorder_traversal(tree.root)
    print()

    result = tree.search_value(30)
    if result:
        print("Node found")
    else:
        print("Node not found")