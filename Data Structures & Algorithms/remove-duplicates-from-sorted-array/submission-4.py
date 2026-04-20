### Two Pointer Approach ###

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # If the array is empty, there are no unique elements
        if not nums:
            return 0

        # L tracks the index of the last unique element found so far
        L = 0

        # R scans through the array starting from the second element
        for R in range(1, len(nums)):
            # If the current element is different from the last unique element,
            # we found a new unique value.
            if nums[R] != nums[L]:
                L += 1 # move to the next position for a unique value
                nums[L] = nums[R] # place the new unique value at the next slot

        # The number of unique elements is the last index + 1
        return L + 1