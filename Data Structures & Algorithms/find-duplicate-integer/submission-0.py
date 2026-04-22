### HashSet Approach ###

"""
1. Initialize HashSet 
2. Loop over the whole array by checking if the current array element in the hash set, as soon as we see that the lement in the hashSet already
we return the integer, because it means it appears in the array multiple times. 
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Initialize HashSet 
        hashset = set()

        # Loop over the array while adding/checking the HashSet 
        for num in nums:
            if num in hashset:
                return num 
            hashset.add(num)
                