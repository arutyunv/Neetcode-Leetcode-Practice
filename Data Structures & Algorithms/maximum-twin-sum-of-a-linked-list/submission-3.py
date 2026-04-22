### Convert to Array Approach ###

"""
A twin sum pairs the i-th node from the start with the i-th node from the end. 
Since linked lists do not support random access, we first convert the list into an array. 
With an array, we can use two pointers starting at opposite ends to easily compute each twin sum and track the maximum.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Step 1. Traverse the array and store each node's value in the array arr 
        arr = [] 
        while head:
            arr.append(head.val)
            head = head.next 

        # Step 2. Initialize two pointers: L=0 at the start and R=len(arr)-1 at the end of the array
        maxSum = 0
        L = 0 
        R = len(arr)-1
        while L<R:
            # Compute sum of two twin nodes 
            sum = arr[L] + arr[R]
            # Check if the sum of the current twin pair > maxSum so far 
            maxSum = max(maxSum, sum)
            # Move both pointers 
            L+=1
            R-=1
        return maxSum 
