### Brute Force Solution ###

"""
A consecutive sequence grows by checking whether the next number (num + 1, num + 2, …) exists in the set.
The brute-force approach simply starts from every number in the list and tries to extend a consecutive streak as far as possible.
For each number, we repeatedly check if the next number exists, increasing the streak length until the sequence breaks.
Even though this method works, it does unnecessary repeated work because many sequences get recomputed multiple times.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # This will store the BEST (longest) sequence length we have found so far
        max_length_of_consecutive_seq = 0

        # Convert list to set for O(1) lookups
        # VERY IMPORTANT:
        # Checking "x in set" is fast so O(1)
        # Checking "x in list" would be slow so O(n)
        new_set = set(nums)

        # Try starting a sequence from EVERY number
        for num in nums:

            # This counts how long the current sequence is
            streak = 0

            # Start from the current number
            current_element = num

            # Keep going while the current number exists in the set
            while current_element in new_set:
                
                # We found a valid next number → increase streak
                streak += 1

                # Move to the next number in sequence
                # Example: 1 → 2 → 3 → 4
                current_element += 1
            
            # After the while loop:
            # we have the FULL streak starting from "num"
            
            # Update the global maximum if this streak is bigger
            max_length_of_consecutive_seq = max(
                max_length_of_consecutive_seq, 
                streak
            )
        
        # Return the longest sequence found
        return max_length_of_consecutive_seq

        