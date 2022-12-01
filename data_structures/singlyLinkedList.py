
# Singly Linked List
# push, pop, insert, remove, get, shift, unshift



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

    def push(self, val:int)->None:
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


    def shift(self) -> int:
        """
        returns the value of head and replaces the head with the next available node
        
        """
        if self.head:
            pop_val = self.head.val
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
            self.length-=1
            return pop_val
            
        else:
            return None



    def unshift(self, val:int) -> Node:
        """
        inserts a node at the beginning of the list
        returns the new Linked list
        """
        if self.head:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
            

        else:
            new_node = Node(val)
            self.head = new_node
            self.tail = new_node
        
        self.length +=1

        return self


        


    def get(self,i:int) -> int:
        """
        returns the ith item's value in the Linked List
        """

        if i <0 or i>self.length-1:
            return None
        
        n = 0
        current_node = self.head
        
        while n <= i:
            if n==i:
                return current_node.val
            current_node = current_node.next
            n+=1
           

    def pop(self)->int:
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

    
    def populate_list(self):
        someList = SinglyLinkedList()
        someList.push(1)
        someList.push(2)
        someList.push(3)
        someList.push(9)
        return someList


    def test_push(self):
        someList = self.populate_list()
       
        self.assertEqual(someList.head.val, 1)
        self.assertEqual(someList.tail.val, 9)

    def test_pop(self):
        someList = self.populate_list()
       
        for i in range(someList.length):
            someList.pop()

        self.assertFalse(someList.pop())


    def test_shift(self):
        someList = self.populate_list()
        self.assertEqual(someList.shift(),1)
        self.assertEqual(someList.length,3)


    def test_unshift(self):
        someList = self.populate_list()
        unshifted = someList.unshift(99)
        self.assertEqual(unshifted.head.val,99)
        self.assertEqual(type(unshifted),SinglyLinkedList)
        self.assertEqual(unshifted.length,5)


    def test_get(self):
        someList = self.populate_list()

        self.assertEqual(someList.get(0),1)
        self.assertEqual(someList.get(3),9)
        self.assertFalse(someList.get(11))
        


if __name__ == "__main__":
    unittest.main()
