import unittest

# to extract a median


class MaxBinaryHeap:
    def __init__(self):
        self.heap = []
        self.length = 0

    def insert(self, value):
        # if root already exists

        def heapify_up(child_idx):

            child = self.heap[child_idx]
            # find parent
            parent_idx = (child_idx - 1) // 2
            parent = self.heap[parent_idx]

            # if already in right place

            if child_idx >= 1:
                if parent >= child:
                    pass
                else:
                    # swap
                    self.heap[parent_idx] = child
                    self.heap[child_idx] = parent
                    heapify_up(child_idx=parent_idx)

        if self.length > 0:
            self.heap.append(value)
            self.length += 1

            # find the parent and child index
            child_idx = self.length - 1

            heapify_up(child_idx)
        else:
            self.heap.append(value)
            self.length += 1

    def extract_max(self):
        root = self.heap[0]
        # assign the new parent
        leaf = self.heap.pop()
        print(f"popped {leaf}")
        # decrement the length
        self.length -= 1

        if self.length == 1:
            print("LAST ELEEMENNT")

        self.heap[0] = leaf
        print(f"{self.heap}")

        # compare if the parent is greater than c1 and c2

        def heapify_down(parent_idx):
            # children indices
            c1, c2 = 2*parent_idx + 1, 2*parent_idx+2

            parent = self.heap[parent_idx]
            # validate if a child exists in that index

            child1 = self.heap[c1] if c1 <= self.length-1 else None
            print(f"index {c1} for child {child1}")

            child2 = self.heap[c2] if c2 <= self.length-1 else None
            print(f"index {c2} for child {child2}")

            if child2 and child1:
                if child2 >= child1:
                    self.heap[c2] = parent
                    self.heap[parent_idx] = child2
                    parent_idx = c2
                else:
                    self.heap[c1] = parent
                    self.heap[parent_idx] = child1
                    parent_idx = c1
            if child2 and not child1:
                self.heap[c2] = parent
                self.heap[parent_idx] = child2
                parent_idx = c2
            if child1 and not child2:
                self.heap[c1] = parent
                self.heap[parent_idx] = child1
                parent_idx = c1
            if not child1 and not child2:
                return None
            heapify_down(parent_idx)

        heapify_down(0)
        return root


class TestMethod(unittest.TestCase):
    def test_base(self):

        base_input = [12, 14, 36, 54]
        heap = MaxBinaryHeap()

        for i in base_input:
            heap.insert(i)

        for i in range(heap.length):
            print(heap.heap)
            current_max = heap.extract_max()
            print("Current Max", current_max)

        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
