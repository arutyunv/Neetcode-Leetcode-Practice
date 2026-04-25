### Two-Pointer Approach ###

"""
After sorting the array, we can fix one number and then search for the other two using the two-pointer technique.
Sorting helps in two ways:

    * It lets us skip duplicates easily.
    * It ensures that moving the left or right pointer will increase or decrease the sum in a predictable way.

For each fixed number a, we place two pointers:

    * l starts just after i,
    * r starts at the end.

If the current sum is too large, we move r left to reduce it.
If the sum is too small, we move l right to increase it.
When the sum is exactly zero, we record the triplet and skip duplicates.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Create an empty list to store all valid triplets
        res = [] 

        # Sort the array so we can use two pointers
        # and skip duplicates more easily
        nums.sort()

        # Loop through each number in the sorted array
        # i = index, a = value at that index
        for i, a in enumerate(nums): 
            
            # If a is already positive, we can stop
            # because nums is sorted, so all numbers after it are also positive
            # Three positive numbers cannot sum to 0
            if a > 0: 
                break 

            # Skip duplicate values for a
            # We do not want to use the same fixed number twice
            # because it would create duplicate triplets
            if i > 0 and a == nums[i - 1]:
                continue

            # Left pointer starts right after i
            # Right pointer starts at the end of the array
            L, R = i + 1, len(nums) - 1

            # Keep searching while the two pointers do not cross
            while L < R:
                # Compute the sum of the fixed number
                # plus the two pointer values
                threeSum = a + nums[L] + nums[R]

                # If the sum is too large,
                # move R left to use a smaller number
                if threeSum > 0:
                    R -= 1

                # If the sum is too small,
                # move L right to use a bigger number
                elif threeSum < 0:
                    L += 1

                # Otherwise, the sum is exactly 0
                # so we found a valid triplet
                else:
                    # Add the triplet to the result list
                    res.append([a, nums[L], nums[R]])

                    # Move both pointers inward
                    # because we already used this pair
                    L += 1
                    R -= 1

                    # if we encounter the same value at Left pointer while moving forward
                    # We skip it to not create a duplicate 
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1

        # Return all unique triplets
        return res

