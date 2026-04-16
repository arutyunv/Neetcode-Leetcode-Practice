### Hash Map Approach ### 

"""
Idea: Use hash map that stores key->value pair as an element->its frequency. While building that, check if any elementss frequncy is larger than n//3.
If it is, then append to result set that will be later converted to list and returned. 

Runtime: O(n), because loop over the whole array once. 
Space: O(n), because create an additional data structure HashMap that takes up to O(n) space. 

"""


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Get the length of array
        n = len(nums)

        # Initialize return set (that will be later converted to list) to avoid duplicates
        return_elements = set()
        # and HashMap to store value->frequency pairs
        frequency_map = {}

        # loop over each element in array nums
        for num in nums:    
            # If that value exists, increment by 1 
            if num in frequency_map:
                frequency_map[num] += 1
            else:
                # If value does not exist yet, create a new key-value pair 
                frequency_map[num] = 1

            # Check if the current element showed up more than n/3 times? 
            if frequency_map[num] > n // 3:
                # If so, append to elements array 
                return_elements.add(num)
        
        # Convert to the return set to list and return 
        return list(return_elements)

        