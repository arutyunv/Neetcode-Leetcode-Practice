### Iterative Version ###

"""
Binary Search (on a sorted array)

1. Find the middle element.
2. Compare it with the target:
   • If middle < target → go RIGHT
   • If middle > target → go LEFT
   • If equal → FOUND
3. Repeat until found or search space is empty.

Key idea:
Each step removes HALF of the remaining array.

Time Complexity:
O(log n)

Requirement:
Array must be SORTED.

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Left pointer starts at beginning
        left = 0

        # Right pointer starts at end
        right = len(nums) - 1

        # Continue while search space exists
        while left <= right:

            # Find middle index
            mid = (left + right) // 2

            # If target found
            if nums[mid] == target:
                return mid

            # If middle value is too small
            # target must be on the right side
            elif nums[mid] < target:
                left = mid + 1

            # If middle value is too large
            # target must be on the left side
            else:
                right = mid - 1

        # Target not found
        return -1
        