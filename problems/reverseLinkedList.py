import unittest


class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self) -> None:
        self.length = 0
        self.head = None
        self.tail = None


    def push(self,value):
        if not self.head:
            # set the head or tail if not initiated
            self.head = Node(value)
            self.tail = self.head
            self.length +=1
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
            self.length +=1


    def get(self, idx):
        # returns the node at a specified index
        if idx == 0:
            return self.head
        elif idx>0 and idx<= self.length-1:
            i = 1
            current_node = self.head
            while i < self.length:
                current_node = current_node.next
                if i == idx:
                    return current_node
                i+=1
        else:
            return None
        
    
    def pop(self):
        prev_node = self.get(self.length-2)
        last_node = self.tail
        self.tail = prev_node
        self.length -=1
        return last_node
        
    def reverse(self):
        
      
        # must assign current node for iteration
        current_node = self.head

        # establish the tail
        # ensure nothing follows the tail
        self.tail = self.head
        # begin the iteration with a prev node
        prev_node = self.tail
        
        
        i = 0
        while i < self.length:
            print("reversing current value",current_node.value)
            # find the next node
            current_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
        
            i+=1
        


class TestMethod(unittest.TestCase):
    def test_base(self):

        ll = LinkedList()
        input_values = [1,2,3,4,5,6]

        for item in input_values:
            ll.push(item)

        ll.reverse()
        self.assertTrue(False)
        



if __name__ == "__main__":
    unittest.main()