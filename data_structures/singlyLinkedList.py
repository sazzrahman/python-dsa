import unittest


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        """
        pushes the value at the end of the current tail
        """
        new_node = Node(val=val)
        # if the list is currently empty:
        if not self.head:
          # push the new node as head and tail
            self.head = new_node
            self.tail = new_node
            self.length += 1

        else:
          # push to the current tail's next node
            self.tail.next = new_node
            # also make the new new node the new tail
            self.tail = new_node
            # increment the length
            self.length += 1

    def pop(self):
        """
        pops the tail value of the list and assigns a new tail
        """

        if self.length == 0:
            return None
        current_node = self.head
        i = 0
        while i < self.length:

            # check if the next node exists
            if current_node.next:
                # if the next node is the tail node
                if not current_node.next.next:
                    self.tail = current_node.next
                    pop_val = current_node.next.val
                    current_node.next = None
                    self.length -= 1
                    return pop_val

                else:
                    current_node = current_node.next
                    i += 1

            else:
                pop_val = self.head.val
                self.head = None
                self.tail = None
                self.length -= 1
                return pop_val


class TestLinkedList(unittest.TestCase):
    def test_push(self):
        someList = SinglyLinkedList()
        someList.push(1)
        someList.push(2)
        someList.push(3)
        someList.push(9)

        self.assertEqual(someList.head.val, 1)
        self.assertEqual(someList.tail.val, 9)

    def test_pop(self):
        someList = SinglyLinkedList()
        someList.push(1)
        someList.push(2)
        someList.push(3)
        someList.push(9)

        for i in range(someList.length):
            someList.pop()

        self.assertFalse(someList.pop())


if __name__ == "__main__":
    unittest.main()
