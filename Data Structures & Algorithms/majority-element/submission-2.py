### Hash Map Solution ###

# Idea: Create a hash map, which stores value -> value's frequency by iterating over array. 
# Track the element with the maximum count seen so far. Once any element's count exceeds n/2, 
# it must be the majority element. 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize a hash map to store element frequencies
        hash_map = {} 

        # Create a placeholder variable to keep track of the majority element
        majority_element = 0
        # Keep track of the max count so far seen
        maxCount = 0 

        # Loop over elements in nums 
        for num in nums: 
            # If element in hash map already, then increment by 1 
            if num in hash_map:
                hash_map[num]+=1
            # if not in the hash map (new element), then create that key-value pair 
            else:
                hash_map[num] = 1
            
            # If count of the element is > maxCount seen so far, then 
            # update maxCount and rememeber that element with maxCount 
            if maxCount < hash_map[num]:
                maxCount = hash_map[num]
                majority_element = num
        
        return majority_element

        # Assuming (as in problem), majority element always exists


        