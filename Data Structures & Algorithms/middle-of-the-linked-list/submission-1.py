### Fast and Slow Pointers Approach ###

"""
1. Have two pointers start at the head of the linked list (one fast + one slow)
2. Move fast pointer twice faster over the LinkedList than the slow pointer 
3. By the time the fast pointer gets to end, the slow pointer would be in the middle of Linked list 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        return slow 