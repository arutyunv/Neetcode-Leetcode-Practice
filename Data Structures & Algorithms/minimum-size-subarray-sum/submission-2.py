### Variable Size Sliding Window ###

"""
Since all elements are positive, we can use a sliding window approach. 
We expand the window by moving the right pointer to increase the sum. Once the sum meets or exceeds the target, we try to shrink the window from the left to find the minimum length. 
This works because removing elements from the left will only decrease the sum, and we want the smallest window that still satisfies the condition.
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # l: left pointer of the sliding window
        # total: current sum of the window
        l, total = 0, 0
        
        # res: stores the minimum length found
        # initialize with infinity (so any real length will be smaller)
        res = float("inf")

        # r: right pointer (we expand the window to the right)
        for r in range(len(nums)):
            
            # Add current element to the window sum
            total += nums[r]

            # If current window sum is valid (≥ target),
            # try to shrink the window from the left
            while total >= target:
                
                # Update result with smaller window size
                res = min(r - l + 1, res)
                
                # Remove leftmost element from the window
                total -= nums[l]
                
                # Move left pointer to shrink window
                l += 1

        # If we never found a valid window - return 0
        # otherwise return the smallest length found
        return 0 if res == float("inf") else res



        