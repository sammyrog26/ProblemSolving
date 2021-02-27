class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # A utility function to check if the list
    #  is palindrome or not
    def isPalindrome(self):
        node = self.head
        length = 0
        comp = []
        while node:
            comp.append(node.data)
            node = node.next
            length += 1

        # Traverse the linked list again checking
        # the elements of our stack(comp)
        node = self.head
        for item in comp[::-1]:
            if item != node.data:
                return False
            node = node.next
        return True


if __name__ == "__main__":
    node = LinkedList()
    node.head = Node('1')
    node.head.next = Node('3')
    node.head.next.next = Node("5")
    node.head.next.next.next = Node("5")
    node.head.next.next.next.next = Node("3")
    node.head.next.next.next.next.next = Node("1")

    if node.isPalindrome():
        print(True)
    else:
        print(False)
