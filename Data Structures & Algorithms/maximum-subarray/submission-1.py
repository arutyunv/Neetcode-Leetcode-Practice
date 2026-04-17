"""
We want the maximum sum of a contiguous subarray.

Kadane’s Algorithm is based on one simple observation:
    * if the running sum becomes negative, keeping it will only reduce the sum of any future subarray
So whenever the current sum drops below zero, we reset it and start a new subarray from the next element.

As we scan the array once, we keep track of:
    * the best subarray sum ending at the current position
    * the best subarray sum seen overall

"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maxSub will store the best (maximum) subarray sum found so far
        # we initialize it to nums[0] to handle all-negative arrays correctly
        maxSub = nums[0]
        
        # curSum keeps track of the current running subarray sum
        curSum = 0

        # iterate through each number in the array
        for num in nums:
            
            # if the current sum becomes negative,
            # it's better to start fresh from the current number
            if curSum < 0:
                curSum = 0
            
            # add the current number to the running sum
            curSum += num
            
            # update maxSub if the current sum is better than what we’ve seen before
            maxSub = max(maxSub, curSum)
        
        # return the maximum subarray sum found
        return maxSub