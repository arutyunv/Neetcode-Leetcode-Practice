### Brute Force Approach ###

"""
Brute Force can be done in 2 steps: 

1. Iterate through the entire list and using variable length calculate the length of the array.
In your first pass you need to know the length of the list, so you traverse it once. 
If you use head to do that traversal, head will end up at the last node (or None) after the loop, and you’ll lose the pointer to the start of the list. 
You then wouldn’t be able to move to the middle from the original head.

2. Run a loop until length//2 and when we exit the loop, we would reach the middle node.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Step 1. Get the length of the Linked List 
        length = 0 
        head1 = head 
        while head1: 
            length += 1
            head1 = head1.next 
        
        # Step 2. Run a loop until length//2 to get the middle element
        for i in range(length//2):
            head = head.next 
        
        return head 
        

        