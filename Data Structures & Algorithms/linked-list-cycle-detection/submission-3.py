### Fast and Slow Pointers (Floyd's Algo) ###

"""
We have two pointers: slow pointer and fast pointer. Fast pointer moves twice faster than slow pointer. 
If there a loop, the fast pointer will eventually lap/intersect the slow pointer -> they must meet somewhere in the cycle -> cycle detected. 

If there is no loop: fast hits None -> stop -> no cycle detected. 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next # move 1 step 
            fast = fast.next.next # move 2 steps 

            if slow == fast: # they meet -> cycle 
                return True 
        
        return False # fast reached none -> no cycle 

        