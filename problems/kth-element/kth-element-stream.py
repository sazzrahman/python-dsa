import unittest

# a good test for extract min and extract max is to check if the numbers are sequential


class MinBinaryHeap:
    def __init__(self) -> None:
        self.heap = []
        self.length = 0

    @staticmethod
    def find_parent(child_idx: int) -> int:
        return (child_idx - 1) // 2

    @staticmethod
    def find_children(parent_idx: int) -> tuple:
        return 2*parent_idx + 1, 2*parent_idx + 2

    def get_child(self, child_idx: int) -> int:
        if child_idx < self.length:
            return self.heap[child_idx]
        else:
            return None

    def heapify_up(self, child_idx: int):
        if child_idx != 0:
            parent_idx = self.find_parent(child_idx)
            child = self.heap[child_idx]
            parent = self.heap[parent_idx]

            if child < parent:
                # swap
                self.heap[child_idx] = parent
                self.heap[parent_idx] = child
                self.heapify_up(parent_idx)

    def heapify_down(self, parent_idx: int) -> None:

        # find children index first
        child_left_idx, child_right_idx = self.find_children(parent_idx)

        parent = self.heap[parent_idx]
        child_left = self.get_child(child_left_idx)
        child_right = self.get_child(child_right_idx)

        # both children exist
        if child_left and child_right:
            if child_left < child_right:
                self.heap[parent_idx] = child_left
                self.heap[child_left_idx] = parent
                self.heapify_down(child_left_idx)
            else:
                self.heap[parent_idx] = child_right
                self.heap[child_right_idx] = parent
                self.heapify_down(child_right_idx)

        # if only left child exists
        elif child_left and not child_right:
            self.heap[parent_idx] = child_left
            self.heap[child_left_idx] = parent
            self.heapify_down(child_left_idx)

        # if only right child exist
        elif child_right and not child_left:
            self.heap[parent_idx] = child_right
            self.heap[child_right_idx] = parent
            self.heapify_down(child_right_idx)

    def insert(self, value: int) -> None:
        """insert a node in minimum binary heap
        """
        self.heap.append(value)
        self.length += 1
        child_idx = self.length - 1
        self.heapify_up(child_idx=child_idx)

    def extract_min(self):
        """extract the root of the minimum heap and heapify
        """
        if self.length >= 2:
            root = self.heap.pop(0)
            self.length -= 1
            leaf = self.heap.pop()
            # insert in the beginning
            self.heap.insert(0, leaf)
            self.heapify_down(parent_idx=0)
            return root
        if self.length == 1:
            root = self.heap.pop(0)
            return root

    def validate(self):
        i = self.length - 1
        while i > 0:
            child = self.heap[i]
            parent_idx = self.find_parent(i)
            parent = self.heap[parent_idx]

            if child > parent:
                pass
            else:
                print(
                    f"INVALID {child} at index {i} > parent {parent} at index {parent_idx}")
            i -= 1


class TestMethod(unittest.TestCase):
    def test_base(self):
        input_stream = [5, 9, 12, 11, 100, 6, 71, 3, 1, 44]

        minheap = MinBinaryHeap()
        for i in input_stream:
            minheap.insert(i)
            print(minheap.heap)
            minheap.validate()

        for i in input_stream:
            print(minheap.extract_min())
            minheap.validate()

        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
