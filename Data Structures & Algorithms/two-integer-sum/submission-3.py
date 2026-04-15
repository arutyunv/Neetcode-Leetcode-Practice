### Hash Map Approach ###

# Idea: 
# We can use a hash map to store the value and index of each element in the array. 
# Then, we can iterate through the array and check if the complement of the current element exists in the hash map. 
# The complement must be at a different index, because we can't use the same element twice.

# By using a hashmap, we can achieve a time complexity of O(n) because the insertion and lookup time of a hashmap is O(1).

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a hash map (dictionary) to store the value and index of each element in the array
        # Store: val -> index
        hash_map = {}

        # Iterate/populate the hash map
        for i, n in enumerate(nums):
            hash_map[n] = i

        # Iterate over the array and compute the complement of the current element, which is target - nums[i]
        for i, n in enumerate(nums):
            diff = target - n 
            # Check if the complement exists in the hash map and indices don't match 
            if diff in hash_map and hash_map[diff] != i:
                # If it does, return the indices of the current element and its complement
                return [i, hash_map[diff]]
        
        # If no such pair is found, return an empty array 
        return []
        

        