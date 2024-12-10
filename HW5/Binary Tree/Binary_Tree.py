class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Add a node to the binary tree using level-order traversal
    def add_node(self, value):
        new_node = Node(value)
        queue = [self]
        while queue:
            current = queue.pop(0)
            if not current.left:
                current.left = new_node
                break
            else:
                queue.append(current.left)

            if not current.right:
                current.right = new_node
                break
            else:
                queue.append(current.right)

    # Search for a value in the binary tree
    @staticmethod
    def __search_in_tree(current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        return (Node.__search_in_tree(current_node.left, value) or
                Node.__search_in_tree(current_node.right, value))

    def contains(self, value):
        return self.__search_in_tree(self, value)

    # Traverse the tree in various orders
    def traverse(self, traversal_type):
        traversal_function = Node.__get_traversal_function(traversal_type)
        traversal_result = []
        traversal_function(self, traversal_result)
        return traversal_result

    @staticmethod
    def __get_traversal_function(traversal_type):
        if traversal_type == "inOrderDFS":
            return Node.__in_order_dfs
        elif traversal_type == "preOrderDFS":
            return Node.__pre_order_dfs
        elif traversal_type == "postOrderDFS":
            return Node.__post_order_dfs
        elif traversal_type == "levelOrder":
            return Node.__level_order_traversal
        else:
            raise ValueError(f"Unsupported traversal type: {traversal_type}")

    @staticmethod
    def __in_order_dfs(node, result):
        if node:
            Node.__in_order_dfs(node.left, result)
            result.append(node.value)
            Node.__in_order_dfs(node.right, result)

    @staticmethod
    def __pre_order_dfs(node, result):
        if node:
            result.append(node.value)
            Node.__pre_order_dfs(node.left, result)
            Node.__pre_order_dfs(node.right, result)

    @staticmethod
    def __post_order_dfs(node, result):
        if node:
            Node.__post_order_dfs(node.left, result)
            Node.__post_order_dfs(node.right, result)
            result.append(node.value)

    @staticmethod
    def __level_order_traversal(nodes_at_current_level, result):
        # Check if a single node object is given instead of a list
        if isinstance(nodes_at_current_level, Node):
            nodes_at_current_level = [nodes_at_current_level]

        nodes_at_next_level = []
        if nodes_at_current_level:
            for node in nodes_at_current_level:
                result.append(node.value)
                if node.left:
                    nodes_at_next_level.append(node.left)
                if node.right:
                    nodes_at_next_level.append(node.right)
            Node.__level_order_traversal(nodes_at_next_level, result)


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)

# Add a new node
root.add_node(60)

# Check if a value exists in the tree
print(root.contains(60))  # Output: True
print(root.contains(70))  # Output: False

# Traverse the tree in various orders
print("In-order:", root.traverse('inOrderDFS'))
print("Pre-order:", root.traverse('preOrderDFS'))
print("Post-order:", root.traverse('postOrderDFS'))
print("Level-order:", root.traverse('levelOrder')) 
