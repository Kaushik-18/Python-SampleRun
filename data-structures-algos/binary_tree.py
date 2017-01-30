class Node:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None


class BinaryTree:
    def insert(self, value, node):
        if node is None:
            return Node(value)

        if node.value > value:
            node.left_node = self.insert(value, node.left_node)

        else:
            node.right_node = self.insert(value, node.right_node)

        return node

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left_node)
            print(node.value)
            self.inorder(node.right_node)

    def delete_node(self, node, value):
        if node is None:
            return node
        if node.value < value:
            node.right_node = self.delete_node(node.right_node, value)
        elif node.value > value:
            node.left_node = self.delete_node(node.left_node, value)
        else:
            # we found the node , node has only one child or no child
            if node.left_node is None:
                node = node.right_node
                return node
            if node.right_node is None:
                node = node.left_node
                return node
            # find minimum in right tree, for node with 2 children
            swap_node = BinaryTree.find_min(node.right_node)
            node.value = swap_node.value
            node.right_node = self.delete_node(node.right_node, node.value)

        return node

    @staticmethod
    def find_left_height(node):
        counter = 0
        while node.left_node:
            counter += 1
            node = node.left_node
        return counter

    @staticmethod
    def find_right_height(node):
        counter = 0
        while node.right_node:
            counter += 1
            node = node.right_node
        return counter

    @staticmethod
    def find_min(node):
        while node.left_node:
            node = node.left_node
        return node

    @staticmethod
    def find_max_height(node):
        left_counter = BinaryTree.find_left_height(node)
        right_counter = BinaryTree.find_right_height(node)
        print(left_counter, right_counter)
        if left_counter >= right_counter:
            return left_counter
        else:
            return right_counter

    MAX_VALUE = 40000
    MIN_VALUE = -40000

    @staticmethod
    def checkBST(node, min, max):
        if root is None:
            return True
        if node.value < min:
            return False
        if node.value > max:
            return False
        return BinaryTree.checkBST(node.left_node, min, node.value) and BinaryTree.checkBST(node.right_node, node.value,
                                                                                            max)


root = Node(40)
tree = BinaryTree()

tree.insert(5, root)
tree.insert(77, root)
tree.insert(43, root)
tree.insert(30, root)
tree.insert(4, root)
tree.insert(3, root)

tree.inorder(root)
print("Min is", tree.find_min(root).value)
print("Height", tree.find_max_height(root))
tree.delete_node(root, 4)
tree.inorder(root)
