### Hash Set Approach ### 

"""
To avoid repeatedly recounting the same sequences, we only want to start counting when we find the beginning of a consecutive sequence.
A number is the start of a sequence if num - 1 is not in the set.
This guarantees that each consecutive sequence is counted exactly once.

Once we identify such a starting number, we simply keep checking if num + 1, num + 2, … exist in the set and extend the streak as far as possible.
This makes the solution efficient and clean because each number contributes to the sequence only one time.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Convert list to a set for O(1) lookup time
        # This allows us to quickly check if a number exists
        numSet = set(nums)

        # This will store the length of the longest consecutive sequence found
        longest = 0

        # Loop through each UNIQUE number (set removes duplicates automatically)
        for num in numSet:
            
            # Check if this number is the START of a sequence
            # If (num - 1) is NOT in the set, so this is the beginning
            if (num - 1) not in numSet:
                
                # Start counting the length of this sequence
                length = 1

                # Keep checking if next numbers exist: num+1, num+2, num+3...
                while (num + length) in numSet:
                    
                    # If next number exists → extend the sequence
                    length += 1

                # After the while loop, we found the FULL sequence length
                # Update the longest sequence seen so far
                longest = max(length, longest)

        # Return the length of the longest consecutive sequence
        return longest
        
        