import unittest


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
            self.size += 1
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            else:
                current_node.next = Node(value)
                self.tail = current_node.next
                self.size += 1

    def traverse(self):
        current_node = self.head
        out_string = f"{current_node.value}"
        while current_node:
            current_node = current_node.next
            if current_node:
                out_string += f"->{current_node.value}"
        return out_string

    def reverse(self):
        """In place reversal of linked list
        """

        def detach(current_node):
            """accepts the current node and splits it into two

            Args:
                current_node (Node): _description_
            """
            # the tail end of severed node
            next_node = current_node.next
            # the severed current node
            current_node.next = None
            return current_node, next_node

        head, remaining = detach(self.head)
        # assign the current tail to the severed head
        self.head = self.tail
        self.tail = head
        prev_head = head
        # loop as long as severed is not None
        while remaining:
            head, remaining = detach(remaining)
            # modify the head next to be the prev head
            head.next = prev_head
            # store the modified head as prev_head
            prev_head = head

    def reversek(self):
        pass


class TestMethod(unittest.TestCase):
    def test_insert(self):

        base_input = [1, 2, 3, 4, 5, 6]
        ll = LinkedList()

        for i in base_input:
            ll.insert(i)

        # after insert assert head and tail
        print(ll.traverse())
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 6)
        self.assertEqual(ll.size, 6)

    def test_reverse(self):
        base_input = [1, 2, 3, 4, 5, 6]
        ll = LinkedList()

        for i in base_input:
            ll.insert(i)

        ll.reverse()
        print(ll.traverse())

        self.assertEqual(ll.head.value, 6)
        self.assertEqual(ll.tail.value, 1)


if __name__ == "__main__":
    unittest.main()
