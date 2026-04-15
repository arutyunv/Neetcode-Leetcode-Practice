### Approach with Sorting ###

## Idea: If we sort the array, the majority element must occupy the middle position. 
# Since it appears more than n/2 times, no matter where the majority element's block starts, it will always include the index n/2. 
# This gives us a simple one-liner solution after sorting.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # We sort in-place the list/array 
        nums.sort()
        # Return the element at index n / 2
        return nums[len(nums) // 2]
        
        