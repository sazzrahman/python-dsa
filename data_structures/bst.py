import unittest


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
        self.length = 0

    def insert_next(self, current_node: Node, next_node: Node) -> None:
        """
        recursively puts the current_node to the bottom of the tree
        """
        if next_node.val < current_node.val:
            # go right
            if next_node.right:
                self.insert_next(current_node, next_node.right)
            else:
                next_node.right = current_node
                self.length += 1

        else:
            # go left
            if next_node.left:
                self.insert_next(current_node, next_node.left)
            else:
                next_node.left = current_node
                self.length += 1

    def find_next(self, val: int, next_node: Node) -> None:

        if next_node.val == val:
            return next_node

        elif next_node.val < val:
            # go right
            if next_node.right:
                return self.find_next(val, next_node.right)
            else:
                return None

        else:
            # go left
            if next_node.left:
                return self.find_next(val, next_node.left)
            else:
                return None

    def insert(self, val: int) -> None:
        new_node = Node(val)
        if self.root:
            self.insert_next(new_node, self.root)
        else:
            self.root = new_node
            self.length += 1

    def find(self, val) -> None:
        if val == self.root.val:
            return self.root

        else:
            return self.find_next(val, self.root)

    def breadth_first_search(self, val: int, queue: list) -> Node:
        # queue must contain the root in the first pass
        # if there are elements in the node
        # q_vals = [i.val for i in queue]
        # print(q_vals)
        if len(queue) > 0:
            current_node = queue.pop()
            if current_node.val == val:
                return current_node

            if current_node.left:
                queue.insert(0, current_node.left)
            if current_node.right:
                queue.insert(0, current_node.right)

            return self.breadth_first_search(val, queue)

        else:
            return None

    def depth_first_search(self, node: Node) -> list:
        pass


class TestBinarySearchTree(unittest.TestCase):

    def test_insert(self):
        someTree = BinarySearchTree()

        someTree.insert(4)
        someTree.insert(9)
        someTree.insert(3)
        someTree.insert(1)

        self.assertEqual(someTree.root.val, 4)
        self.assertEqual(someTree.root.right.val, 9)
        self.assertEqual(someTree.root.left.val, 3)
        self.assertEqual(someTree.root.left.left.val, 1)

    def test_find(self):
        someTree = BinarySearchTree()

        someTree.insert(4)
        someTree.insert(9)
        someTree.insert(3)
        someTree.insert(1)

        self.assertEqual(someTree.find(4).val, someTree.root.val)
        self.assertEqual(someTree.find(1).val, someTree.root.left.left.val, 1)
        self.assertFalse(someTree.find(99))

    def test_bfs(self):
        someTree = BinarySearchTree()

        someTree.insert(4)
        someTree.insert(9)
        someTree.insert(3)
        someTree.insert(1)
        someTree.insert(22)
        someTree.insert(36)

        queue = [someTree.root]
        someTree.breadth_first_search(99, queue)
        self.assertFalse(someTree.find(99))


if __name__ == "__main__":
    unittest.main()
