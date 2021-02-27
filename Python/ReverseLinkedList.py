"""
Reverse a Linked List
"""

def reverse(head):
    current = head
    prev = None
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    print(head)

