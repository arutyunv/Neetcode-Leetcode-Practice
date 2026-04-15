### Sorting Approach ###

"""
If we sort the numbers first, then all consecutive values will appear next to each other.
This makes it easy to walk through the sorted list and count how long each consecutive sequence is.
We simply move forward while the current number matches the expected next value in the sequence.
Duplicates don’t affect the result—they are just skipped—while gaps reset the streak count.
This approach is simpler and more organized than the brute force method because sorting places all potential sequences in order.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Edge case: empty list, so no sequence
        if not nums:
            return 0
        
        # Sort numbers so consecutive numbers are next to each other
        nums.sort()

        # Start with streak = 1 (at least one number exists)
        longest = 1
        current_streak = 1

        # Go through array starting from second element
        for i in range(1, len(nums)):
            
            # If duplicate - skip (do nothing)
            if nums[i] == nums[i - 1]:
                continue
            
            # If consecutive - extend streak
            elif nums[i] == nums[i - 1] + 1:
                current_streak += 1
            
            # Otherwise - reset streak
            else:
                current_streak = 1
            
            # Update best result
            longest = max(longest, current_streak)

        return longest
        

