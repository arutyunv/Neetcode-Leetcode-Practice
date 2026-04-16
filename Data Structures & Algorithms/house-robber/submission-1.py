
"""
We can build a decision tree, where at each level, we choose to rob the current house and skip the next house OR skip the current house by robbing previos one and the next one. 

Since we want to optimize by max in those choices, we can construct a recursive relation: money = max(nums[i] + dfs(i+2), dfs(i+1)), where i is the current house and 
dfs() is the recursive function. 

Base cases: 0 when i goes out of bounds. 

Since we can recompute dfs(value) (ex. dfs(5)) multiple times while exploring different paths in the decision tree, 
we need to use the memoization for that. 
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Dictionary to store already computed results
        # key = index, value = max amount of money
        memo = {}

        # Get the length of the array 
        n = len(nums)

        # Recursive helper function
        def dfs(i):
            
            # If we already solved this subproblem (calculated the max amount of money for this house) so reuse result
            if i in memo:
                return memo[i]
            
            # If i is out of bounds, return 0
            if i >= n:
                return 0

            # Find which action: skip or rob better to take? 
            else:
                skip = dfs(i + 1)
                rob = nums[i] + dfs(i + 2)
                res = max(skip, rob)

            #Store and return max(skip, rob) in memo[i].  
            memo[i] = res
            return res

        # Start recursion from 0 index
        return dfs(0)