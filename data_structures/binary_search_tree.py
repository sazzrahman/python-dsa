import unittest

# binary search tree can be really deep with one child but it may not be very compact
# we utilize a queue to remember and include all the nodes


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
        self.length = 0

    def insert(self, value: int):
        if self.root:
            self.insert_next(value, self.root)
        else:
            self.root = Node(value)
            self.length += 1

    def insert_next(self, value: int, current_node: Node):
        """
        finds the next suitable Node for the current value
        """
        if value <= current_node.value:
            # turn left
            if current_node.left:
                return self.insert_next(value, current_node.left)
            else:
                current_node.left = Node(value)
                self.length += 1
        else:
            if current_node.right:
                return self.insert_next(value, current_node.right)
            else:
                current_node.right = Node(value)
                self.length += 1

    def bfs(self, value):
        # explain why we need to utilize a queue to traverse and search the tree in BFS
        # the queue remembers to check the other nodes in queue order

        queue = []
        visited = []
        queue.append(self.root)
        while len(queue) > 0:

            current_node = queue.pop(0)
            visited.append(current_node.value)
            print(visited)
            if current_node.value == value:
                return current_node.value
            else:
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
        return -1

    def dfs_preorder(self):
        visited = []

        def helper(node: Node):
            # we visit the node before visiting its children
            visited.append(node.value)
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
        helper(self.root)

        return visited

    def dfs_postorder(self):
        visited = []

        def helper(node: Node):
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
            # we visit the node after visiting its children
            visited.append(node.value)
        helper(self.root)

        return visited

    def dfs_inorder(self):
        visited = []

        def helper(node: Node):
            if node.left:
                helper(node.left)
            # we visit the node after exploring all the left
            visited.append(node.value)
            if node.right:
                helper(node.right)
        helper(self.root)

        return visited


class TestMethod(unittest.TestCase):
    def test_insert(self):
        bst = BinarySearchTree()
        # compact tree
        input_list = [5, 3, 7, 1, 4, 6, 8]
        for item in input_list:
            bst.insert(item)

        print(bst.dfs_preorder())
        print(bst.dfs_inorder())
        print(bst.dfs_postorder())


if __name__ == "__main__":
    unittest.main()
