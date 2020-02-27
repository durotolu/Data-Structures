# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        curr_node = self
        def inset_helper(value, curr_node):
            if value < curr_node.value:
                if curr_node.left is None:
                    curr_node.left = BinarySearchTree(value)
                    return
                curr_node = curr_node.left
                inset_helper(value, curr_node)
            elif value >= curr_node.value:
                if curr_node.right is None:
                    curr_node.right = BinarySearchTree(value)
                    return
                curr_node = curr_node.right
                inset_helper(value, curr_node)
        inset_helper(value, curr_node)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        curr_node = self
        def contains_recursor(target, curr_node):
            if target == curr_node.value:
                return True
            elif target < curr_node.value:
                if curr_node.left is None:
                    return False
                curr_node = curr_node.left
                return contains_recursor(target, curr_node)
            else:
                if curr_node.right is None:
                    return False
                curr_node = curr_node.right
                return contains_recursor(target, curr_node)
        return contains_recursor(target, curr_node)

    # Return the maximum value found in the tree
    def get_max(self):
        curr_node = self
        def get_max_recursor(curr_node):
            if curr_node.right is None:
                return curr_node.value
            else:
                return get_max_recursor(curr_node.right)
        return get_max_recursor(curr_node)

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        curr_node = self
        cb(curr_node.value)
        def for_each_recursor(curr_node, cb):
            if curr_node is None:
                return
            else:
                cb(curr_node.value)
                for_each_recursor(curr_node.right, cb)
                for_each_recursor(curr_node.left, cb)
                return
        return for_each_recursor(curr_node, cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if node is None:
            return

        queue = []
        queue.append(node)
        while len(queue) > 0:
            print(queue[0].value)
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        if node is None:
            return
        queue = []
        queue.append(node)
        while len(queue):
            curr_node = queue[0]
            queue.pop(0)
            print(curr_node.value)
            children = []
            if curr_node.left:
                children.append(curr_node.left)
            if curr_node.right:
                children.append(curr_node.right)
            for child in range(len(children)-1, -1, -1):
                queue.insert(0, children[child])

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node is None:
            return
        print(node.value)
        self.pre_order_dft(node.left)
        self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node is None:
            return
        self.post_order_dft(node.left)
        self.post_order_dft(node.right)
        print(node.value)


bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.post_order_dft(bst)