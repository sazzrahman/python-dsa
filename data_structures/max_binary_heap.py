import unittest


class MaxBinaryHeap:
    def __init__(self) -> None:
        self.heap = []

    def insert(self, value: int):
        # heap insertion does not follow any specific index
        # append the new value at the end of the array
        self.heap.append(value)
        current_length = len(self.heap)
        if current_length >= 2:
            return self.bubble_up(current_length-1, value)
        else:
            # if the length is 0 or 1 return the heap
            return self.heap

    def bubble_up(self, child_idx, child):
        # restructures the tree by bubbling up elements
        parent_idx, parent = self.find_parent(child_idx)
        if child >= parent:
            # swap
            self.heap[parent_idx] = child
            self.heap[child_idx] = parent
            if parent_idx == 0:
                return self.heap
            else:
                # child has taken over parent idx
                # recurse through the next parent
                return self.bubble_up(parent_idx, child)
        else:
            # the child is in right place
            return self.heap

    def find_parent(self, child_idx):
        parent_idx = (child_idx-1)//2
        return parent_idx, self.heap[parent_idx]

    def find_children(self, idx):
        left_child_idx = 2*idx - 1
        right_child_idx = 2*idx + 1
        return self.heap[left_child_idx], self.heap[right_child_idx]


class TestMethod(unittest.TestCase):
    def test_base(self):

        heap = MaxBinaryHeap()

        first_item = heap.insert(5)
        print(first_item)

        for item in [2,9,11,0,33,67,19]:
            current_heap = heap.insert(item)
            print(current_heap)

        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
