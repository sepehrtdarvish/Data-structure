# Sepehr Darvishi 40216153

import tkinter as tk
from graphviz import Digraph
from tkinter import ttk

class Node:
    def __init__(self, key):
        self.key = key
        self.color = 'RED' 
        self.left = None
        self.right = None
        self.parent = None

    def is_left_child(self):
        return self.parent and self.parent.left == self


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None) 
        self.NIL.color = 'BLACK'
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x.is_left_child():
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x.is_left_child():
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y

    def insert(self, key):
        new_node = Node(key)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = 'RED'
        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node.parent and node.parent.color == 'RED':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.left_rotate(node.parent.parent)
        self.root.color = 'BLACK'

    def search(self, key):
        return self._search_tree(self.root, key)

    def _search_tree(self, node, key):
        while node != self.NIL:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def delete(self, key):
        node_to_remove = self.search(key)
        if node_to_remove == self.NIL:
            return

        original_color = node_to_remove.color
        if node_to_remove.left == self.NIL:
            replacement = node_to_remove.right
            self._transplant(node_to_remove, node_to_remove.right)
        elif node_to_remove.right == self.NIL:
            replacement = node_to_remove.left
            self._transplant(node_to_remove, node_to_remove.left)
        else:
            successor = self._minimum(node_to_remove.right)
            original_color = successor.color
            replacement = successor.right
            if successor.parent == node_to_remove:
                replacement.parent = successor
            else:
                self._transplant(successor, successor.right)
                successor.right = node_to_remove.right
                successor.right.parent = successor
            self._transplant(node_to_remove, successor)
            successor.left = node_to_remove.left
            successor.left.parent = successor
            successor.color = node_to_remove.color

        if original_color == 'BLACK':
            self.fix_delete(replacement)

    def fix_delete(self, node):
        while node != self.root and node.color == 'BLACK':
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == 'RED':
                    sibling.color = 'BLACK'
                    node.parent.color = 'RED'
                    self.left_rotate(node.parent)
                    sibling = node.parent.right
                if sibling.left.color == 'BLACK' and sibling.right.color == 'BLACK':
                    sibling.color = 'RED'
                    node = node.parent
                else:
                    if sibling.right.color == 'BLACK':
                        sibling.left.color = 'BLACK'
                        sibling.color = 'RED'
                        self.right_rotate(sibling)
                        sibling = node.parent.right
                    sibling.color = node.parent.color
                    node.parent.color = 'BLACK'
                    sibling.right.color = 'BLACK'
                    self.left_rotate(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == 'RED':
                    sibling.color = 'BLACK'
                    node.parent.color = 'RED'
                    self.right_rotate(node.parent)
                    sibling = node.parent.left
                if sibling.right.color == 'BLACK' and sibling.left.color == 'BLACK':
                    sibling.color = 'RED'
                    node = node.parent
                else:
                    if sibling.left.color == 'BLACK':
                        sibling.right.color = 'BLACK'
                        sibling.color = 'RED'
                        self.left_rotate(sibling)
                        sibling = node.parent.left
                    sibling.color = node.parent.color
                    node.parent.color = 'BLACK'
                    sibling.left.color = 'BLACK'
                    self.right_rotate(node.parent)
                    node = self.root
        node.color = 'BLACK'

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u.is_left_child():
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def visualize_tree(self):
        graph = Digraph()
        graph.attr('node', shape='circle')

        def add_nodes_edges(node):
            if not node or node == self.NIL:
                return
            node_color = node.color
            graph.node(str(node.key), f"{node.key}", color="red" if node_color == 'RED' else "black", fontcolor="black" if node_color == 'BLACK' else "red")
            
            if node.left and node.left != self.NIL:
                graph.edge(str(node.key), str(node.left.key))
                add_nodes_edges(node.left)
            if node.right and node.right != self.NIL:
                graph.edge(str(node.key), str(node.right.key))
                add_nodes_edges(node.right)

        add_nodes_edges(self.root)
        
        graph.render("temp_tree", format="png", cleanup=True)
        return "temp_tree.png"


class RBTreeApp:
    def __init__(self, root):
        self.tree = RedBlackTree()
        self.root = root
        self.root.title("Red-Black Tree Visualization")
        self.root.geometry("850x700")
        self.root.config(bg="#f2f2f2")
        self.root.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # Main frame for layout
        main_frame = tk.Frame(self.root, bg="#f2f2f2")
        main_frame.pack(fill="both", expand=True)

        # Canvas for drawing tree
        self.tree_canvas = tk.Canvas(main_frame, width=600, height=400, bg="#ffffff", bd=0, relief="flat")
        self.tree_canvas.pack(pady=20)

        # Input section frame
        input_frame = tk.Frame(main_frame, bg="#f2f2f2")
        input_frame.pack(pady=20)

        # Label for input value
        self.entry_label = tk.Label(input_frame, text="Enter Value:", font=("Helvetica", 16, "bold"), bg="#f2f2f2", fg="#2c3e50")
        self.entry_label.grid(row=0, column=0, padx=10)

        # Entry for user input
        self.entry = tk.Entry(input_frame, font=("Helvetica", 14), width=15, bd=2, relief="solid", highlightthickness=1, highlightcolor="#4CAF50")
        self.entry.grid(row=0, column=1, padx=10)

        # Insert button
        self.insert_button = ttk.Button(input_frame, text="Insert", command=self.insert_value, style="TButton")
        self.insert_button.grid(row=1, column=0, padx=10, pady=10)

        # Delete button
        self.delete_button = ttk.Button(input_frame, text="Delete", command=self.delete_value, style="TButton")
        self.delete_button.grid(row=1, column=1, padx=10, pady=10)

        # Search label
        self.search_label = tk.Label(input_frame, text="Search Value:", font=("Helvetica", 16, "bold"), bg="#f2f2f2", fg="#2c3e50")
        self.search_label.grid(row=2, column=0, padx=10)

        # Entry for search input
        self.search_entry = tk.Entry(input_frame, font=("Helvetica", 14), width=15, bd=2, relief="solid", highlightthickness=1, highlightcolor="#4CAF50")
        self.search_entry.grid(row=2, column=1, padx=10)

        # Search button
        self.search_button = ttk.Button(input_frame, text="Search", command=self.search_value, style="TButton")
        self.search_button.grid(row=2, column=2, padx=10, pady=10)

        # Style for buttons (modern and colorful)
        self.style = ttk.Style()
        self.style.configure("TButton",
                             font=("Helvetica", 14),
                             padding=10,
                             relief="raised",
                             background="#3498db",
                             foreground="black")
        self.style.map("TButton", background=[('active', '#2980b9'), ('pressed', '#1c6f8c')])

        # Update the tree visualization
        self.update_tree()

    def update_tree(self):
        image_path = self.tree.visualize_tree()
        tree_image = tk.PhotoImage(file=image_path)
        self.tree_canvas.create_image(0, 0, anchor="nw", image=tree_image)
        self.tree_canvas.image = tree_image

    def insert_value(self):
        try:
            value = int(self.entry.get())
            self.tree.insert(value)
            self.update_tree()
        except ValueError:
            self.show_error("Please enter a valid integer value.")

    def delete_value(self):
        try:
            value = int(self.entry.get())
            self.tree.delete(value)
            self.update_tree()
        except ValueError:
            self.show_error("Please enter a valid integer value.")

    def search_value(self):
        try:
            value = int(self.search_entry.get())
            result_node = self.tree.search(value)
            if result_node:
                self.show_message(f"Value {value} found in the tree.")
            else:
                self.show_error(f"Value {value} not found in the tree.")
        except ValueError:
            self.show_error("Please enter a valid integer value for search.")

    def show_message(self, message):
        message_window = tk.Toplevel(self.root)
        message_window.title("Search Result")
        message_window.geometry("300x150")
        message_window.config(bg="#2ecc71")
        message_label = tk.Label(message_window, text=message, font=("Helvetica", 14), fg="white", bg="#2ecc71")
        message_label.pack(pady=30)
        ok_button = ttk.Button(message_window, text="OK", command=message_window.destroy, style="TButton")
        ok_button.pack(pady=5)

    def show_error(self, message):
        error_window = tk.Toplevel(self.root)
        error_window.title("Error")
        error_window.geometry("300x150")
        error_window.config(bg="#e74c3c")
        error_label = tk.Label(error_window, text=message, font=("Helvetica", 14), fg="white", bg="#e74c3c")
        error_label.pack(pady=30)
        ok_button = ttk.Button(error_window, text="OK", command=error_window.destroy, style="TButton")
        ok_button.pack(pady=5)

root = tk.Tk()
app = RBTreeApp(root)
root.mainloop()