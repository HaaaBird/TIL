# LinkedList.py

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)
    
    def __str__(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
        return "end" 
    

if __name__ == "__main__":
    a_list = LinkedList()
    a_list.append("day1")
    a_list.append("day2")
    print(a_list)
    
    pass