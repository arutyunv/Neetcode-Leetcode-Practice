### Brute Force Solution ### 

"""
Brute Force soltion is simply checking every pair of integers (heights) in the array and for each pair, 
we compute the amount of water it can store. 

Time Complexity: O(n^2)
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Initialize maxAmount variable that would be returned
        maxAmount = 0

        for i in range(len(heights)):
            for j in range(i+1, len(heights)): 
                # find height of the rectangle over y-axis 
                w = min(heights[i], heights[j])
                # find length of rectangle over x-axis 
                l = j - i
                # find current amount of watr in the current rectangle
                curAmount = l * w 
                maxAmount = max(curAmount, maxAmount)

        return maxAmount
