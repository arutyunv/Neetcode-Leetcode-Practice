### More Interesting Approach w/ Hash Set ###

# Instead of checking each element manually, we simply compare the length of the set to the length of the original array.
# If duplicates exist, the set will contain fewer elements.

# Same idea as before, but shorter and more concise implementation of it

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Convert the array into a hash set, which removes duplicates.
        # Converting to set removed duplicates 
        nums_set = set(nums)
    
        return len(nums_set) < len(nums)
        