import unittest
import math


class MaxHeap:
    def __init__(self):
        self.heap = []

    def __str__(self):

        return self.heap

    def insert(self, value):
        self.heap.append(value)
        last_child_value = self.heap[-1]
        last_child_idx = len(self.heap) - 1

        def bubble_up(last_child_idx, last_child_value):
            if last_child_idx == 0:
                pass
            else:
                parent_idx = (last_child_idx - 1) // 2
                parent_value = self.heap[parent_idx]

                if parent_value <= last_child_value:
                    self.heap[parent_idx] = last_child_value
                    self.heap[last_child_idx] = parent_value
                    bubble_up(last_child_idx=parent_idx,
                              last_child_value=last_child_value)

        bubble_up(last_child_idx, last_child_value)

    def print_tree(self):

        def print_node(p):
            c1 = 2*p + 1
            c2 = 2*p + 2
            if c2 < len(self.heap):
                print(self.heap[p], "--->", self.heap[c1], "||", self.heap[c2])
                print_node(c1)
                print_node(c2)

        print_node(0)

    def delete(self):
        pass


class TestMethod(unittest.TestCase):
    def test_base(self):

        test_input = [7, 8, 9, 1, 2, 3, 0, 11, 33, 88]

        mh = MaxHeap()
        for item in test_input:
            mh.insert(item)

        print(mh)
        mh.print_tree()
        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
