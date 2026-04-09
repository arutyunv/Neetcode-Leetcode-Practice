# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        curr1, curr2 = list1, list2
        while curr1:
            nodes.append(curr1)
            curr1 = curr1.next
        while curr2:
            nodes.append(curr2)
            curr2 = curr2.next
        
        if not nodes:
            return None
            
        nodes.sort(key=lambda x: x.val)
        
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i+1]
        nodes[-1].next = None
        
        return nodes[0]