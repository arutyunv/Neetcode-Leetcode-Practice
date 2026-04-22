### Fast and Slow Pointers ###

"""
Treat the array like a linked list, where each index points to the next index given by its value.
Because one number is duplicated, two indices will point into the same chain, creating a cycle — exactly like a linked list with a loop.

Using Floyd’s Fast & Slow Pointer technique:

    1. The slow pointer moves one step at a time.
    2. The fast pointer moves two steps at a time.
If there’s a cycle, they will eventually meet.
Once they meet, we start a new pointer from the beginning:
    1. Move both pointers one step at a time.
    2. The point where they meet again is the duplicate number (the entry point of the cycle).
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 2. Initialize two pointers slow = 0 and fast = 0.
        slow, fast = 0, 0
        while True:
            # Move pointers 
            slow = nums[slow]
            fast = nums[nums[fast]]
            # until they meet 
            if slow == fast:
                break

        # Start a new pointer slow2 = 0 
        slow2 = 0
        while True:
            # Move both pointers until they meet 
            slow = nums[slow]
            slow2 = nums[slow2]
            # the meeting point is the duplicate number 
            if slow == slow2:
                # return that number 
                return slow
        