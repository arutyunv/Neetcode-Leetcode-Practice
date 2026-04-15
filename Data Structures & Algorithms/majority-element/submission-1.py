### Hash Map Solution ###

# Idea: Create a hash map, which stores value -> value's frequency by iterating over array. 
# Track the element with the maximum count seen so far. Once any element's count exceeds n/2, 
# it must be the majority element. 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize a hash map to store element frequencies
        hash_map = {} 
        majority_element = 0
        maxCount = 0 

        for num in nums: 
            if num in hash_map:
                hash_map[num]+=1
            else:
                hash_map[num] = 1
            
            if maxCount < hash_map[num]:
                maxCount = hash_map[num]
                majority_element = num
        
        return majority_element


        