# Definition for a singly-linked list node
# We must define what the node is 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        # Head points to the first node, which is None
        # head gives you access to the whole list
        # head -> None 
        self.head = None

        # but when you do, self.head = ListNode(5)
        # you have: head -> [5 | None]

        self.size = 0

    def get(self, index: int) -> int:
        # Return the value at position index 
        # example: Linked List: 10 -> 20 -> 30 -> 40
        # want: get(2), should return 30

        # Note: unlike arrays, linkedLists do not have direct indexing
        # therefore, start from head and walk step by step

        # Start from the head node
        current = self.head

        # Step counter to track position
        i = 0

        # Traverse the list
        while current:
            
            # If we reached the desired index, then return value
            if i == index:
                return current.val
            
            # Move to next node
            current = current.next
            
            # Increase step counter
            i += 1
        
        # If index is out of bounds → return -1
        return -1
    
    def addAtTail(self, val: int) -> None:
        # Create the new node we want to add
        new_node = ListNode(val)

        # If the list is empty, this new node becomes the head
        if not self.head:
            self.head = new_node
            return

        # Otherwise, walk to the last node
        current = self.head
        while current.next:
            current = current.next

        # Link the last node to the new node
        current.next = new_node


    def addAtHead(self, val: int) -> None:
        # Add a node of value val before the first element of the linked list. 
        # After the insertion, the new node will be the first node of the linked list

        # Create a new node (using class ListNode)
        new_node = ListNode(val)

        # New node should point to the current head
        new_node.next = self.head

        # Update head to this new node
        self.head = new_node


    def addAtIndex(self, index: int, val: int) -> None:
        # If index is 0, inserting at head is the correct operation
        if index == 0:
            self.addAtHead(val)
            return

        # Start from the head
        current = self.head
        i = 0

        # We want to stop at the node JUST BEFORE the insertion position
        # For example, to insert at index 2, stop at index 1
        while current and i < index - 1:
            current = current.next
            i += 1

        # If current is None, index is bigger than the length of the list
        # so we do nothing
        if not current:
            return

        # Create the new node
        new_node = ListNode(val)

        # New node points to what current was previously pointing to
        new_node.next = current.next

        # Current now points to the new node
        current.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        # If list is empty, nothing to delete
        if not self.head:
            return

        # If deleting the head node
        if index == 0:
            self.head = self.head.next
            return

        # Start from the head
        current = self.head
        i = 0

        # Stop at the node JUST BEFORE the one we want to delete
        while current and i < index - 1:
            current = current.next
            i += 1

        # If current is None, or current.next is None,
        # then index is invalid
        if not current or not current.next:
            return

        # Skip over the node at 'index'
        current.next = current.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
