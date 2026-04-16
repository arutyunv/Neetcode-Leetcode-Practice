### Sorting Approach ### 

"""
After soring, identical elements are grouped togther. We can scan through and count consecutive runs of each elements.
If a run's length > n/3? we add the element to our result. This appriach avoids the nexted loops of brute force. 

Runtime: O(nlogn) because we sorted it 
Space: O(n), because sorting (even if you call sort in place) may use O(n) extra space internally.

"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Sorting an array nums in place
        nums.sort()
        # Initialize result array that will be returned
        return_elements = []
        # get the length of the initial array 
        n = len(nums)
        
        # One pointer that goes throug the array 
        i = 0 
        while i < n:
            # one pointer that 1 index ahead 
            j = i + 1
            # as long as the next element is the same, we move second pointer and count the consecutive sequence length 
            while j < n and nums[i] == nums[j]:
                j+=1
            # if the consecutive sequence length is > n/3, we append the element to the result array
            if (j - i) > n//3:
                return_elements.append(nums[i])
            
            # reset the first pointer to the second pointer to proceed with correct tracing 
            i = j
        
        # return the resulting elements 
        return return_elements