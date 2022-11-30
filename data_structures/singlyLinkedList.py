
class Node:    
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
 
class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def push(self,val):
        """
        pushes the value at the end of the current tail
        """
        new_node = Node(val=val)
        # if the list is currently empty:
        if not self.head:
          # push the new node as head and tail
            self.head = new_node
            self.tail = new_node
            self.length+=1
        
        else:
          # push to the current tail's next node
          self.tail.next = new_node
          # also make the new new node the new tail
          self.tail = new_node
          # increment the length
          self.length += 1
        

if __name__ == "__main__":
    print("Running test case")
    someList = SinglyLinkedList()
    
    
    someList.push(1)
    someList.push(2)
    someList.push(3)

    print(someList.head.val, someList.tail.val)
    


            

