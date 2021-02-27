class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traverseList(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def insertNode(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode


if __name__ == "__main__":
    ll = LinkedList()
    ll.insertNode(1)
    ll.insertNode(10)
    ll.insertNode(101)
    ll.traverseList()
