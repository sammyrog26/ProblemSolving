"""
Reverse a Linked List
        a           b           c          d          e          f
    [None, 1]---->[a, 3]---->[b, 5]---->[c, 4]---->[d, 2]---->[e, 1]

       f           e           d           c         b          a
    [None, 1]---->[f, 2]---->[e, 4]---->[d, 5]---->[c, 3]---->[b, 1]
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Function to reverse the linked list
    def reverse_link_list(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(85)
    print("LinkedList:")
    llist.print_list()
    llist.reverse_link_list()
    print("\nReversed LinkedList:")
    llist.print_list()