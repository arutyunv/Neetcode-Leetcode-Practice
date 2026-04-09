## RECURSIVE APPROACH ### 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base Case: If list is empty, then nothing to reverse
        # So recursion stops going deeper
        if not head:
            return None

        # Assume current head is a new head (that might be overwritten later)
        newHead = head

        # If there is a next node:
        # means we are not at the last node
        # so we can recurse deeper        
        if head.next:
            # Reversing everything after first
            newHead = self.reverseList(head.next)
            # Reversion proceduree 
            head.next.next = head
        # Cut the old connection
        head.next = None

        # Always return the LAST node (which became first)
        return newHead