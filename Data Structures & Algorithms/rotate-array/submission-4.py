### Three Reversals Approach ###

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Get the size of the array 
        n = len(nums)

        # If k is larger than array size,
        # reduce it because rotating n times gives same array
        k = k % n


        def reverse(L, R):
            """
            Reverse elements between left and right in-place.

            VIA TWO POINTERS! 
            """
            while L < R:
                nums[L], nums[R] = nums[R], nums[L]
                L += 1
                R -= 1

        
        # Step 1. Reverse the entire array 
        reverse(0, n-1)

        # Step 2. Reverse the first k elements 
        reverse(0, k-1)

        # Step 3. Reverse the rest
        reverse(k, n-1)

        