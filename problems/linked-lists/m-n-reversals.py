
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

    def insert(self, value: int) -> None:
        if not self.head:
            self.head = Node(value)
            self.tail = Node(value)
            self.size += 1

        else:
            current_node = self.head
            while current_node.next:

                current_node = current_node.next
            else:
                current_node.next = Node(value)
                self.tail = current_node.next
                self.size += 1

    @staticmethod
    def detach(node: Node):
        """_summary_
        Detaches the current node into the first node and remaining node

        Args:
            node (Node): _description_

        Returns:
            _type_: _description_
        """
        current_node, next_node = node, node.next
        # empty the next value for current node
        current_node.next = None
        return current_node, next_node

    def reverse(self, node: Node) -> None:
        """reverses a the linked list given the Head
        Args: node: Current head of a reverse

        Does not alter head or tail
        """
        prev_node, remaining = self.detach(node)
        while remaining:
            current_node, remaining = self.detach(remaining)
            current_node.next = prev_node
            prev_node = current_node

        return prev_node

    def split(self, node: Node, m: int) -> tuple:
        """splits a linked list on node m
        returns: 
        Node at m-1
        head Node at 1
        Node at m

        Args:
            node (Node): _description_
            m (int): Node m in sequence 1 to m
        """
        current_node = node
        left_list = node
        right_list = None
        i = 1

        while current_node:
            if i == m-1:
                right_list = current_node.next
                current_node.next = None
                return left_list, current_node, right_list

            else:
                current_node = current_node.next
                i += 1

    def reverse_mn(self, node: Node, m: int, n: int):

        left_list, tail_node_m, right_list = self.split(node, m)

        mid_list, tail_node_n, right_list = self.split(right_list, n)

        reversed_mid_list = self.reverse(mid_list)

        tail_node_m.next = reversed_mid_list
        reversed_mid_list.next = right_list
        return left_list

    def traverse(self, node: Node) -> None:
        """
        For any given node, it reverse the node

        Args:
            node (Node): _description_

        Returns:
            _type_: _description_
        """

        current_node = node
        s = f"{node.value}"

        while current_node:
            # move to the next node
            current_node = current_node.next
            if current_node:
                s += f"->{current_node.value}"

        return s


class TestMethod(unittest.TestCase):

    # test cases
    # m and n can be outside of linked list.
    # m = 1 and n = len(linked list)

    def test_reverse(self):

        input_base = [1, 2, 3, 4, 5, 6]

        ll = LinkedList()

        for i in input_base:
            ll.insert(i)

        print(ll.traverse(ll.head))

        reversed = ll.reverse(ll.head)

        print(ll.traverse(reversed))

        self.assertEqual(ll.size, 6)

    def test_split(self):
        input_base = [1, 2, 3, 4, 5, 6]

        ll = LinkedList()

        for i in input_base:
            ll.insert(i)

        # print a forward list
        print(ll.traverse(ll.head))
        left_list, tail_list, right_list = ll.split(ll.head, 3)

        print(ll.traverse(left_list))
        print(ll.traverse(tail_list))
        print(ll.traverse(right_list))

    def test_reverse_mn(self):
        pass


if __name__ == "__main__":

    unittest.main()
