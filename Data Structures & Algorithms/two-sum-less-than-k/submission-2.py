### Two-Pointer Approach ### 

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # First, sort the array so we can use the two-pointer technique
        nums.sort()

        # Initialize two pointers:
        # L starts at the beginning (smallest value)
        # R starts at the end (largest value)
        L = 0 
        R = len(nums) - 1
        
        # This will store the maximum valid sum < k
        # If no such pair exists, we return -1
        maxSum = -1

        # Continue while the two pointers do not cross
        while L < R:
            # Calculate current sum of the two numbers
            current_sum = nums[L] + nums[R]

            # If the sum is less than k, it's a valid candidate
            if current_sum < k:
                # Update maxSum if this is the largest valid sum so far
                maxSum = max(maxSum, current_sum)

                # Move left pointer to the right to try a bigger sum
                # (since array is sorted, nums[L+1] is larger)
                L += 1
            else:
                # If sum is >= k, it's too large
                # Move right pointer to the left to reduce the sum
                R -= 1

        # Return the best valid sum found (or -1 if none exists)
        return maxSum
