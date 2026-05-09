class Solution:
    def rob(self, nums: List[int]) -> int:
        # Dictionary to store already computed results
        # key = index, value = max amount of money
        memo = {}

        # Get the length of the array 
        n = len(nums)
        
        if n == 1:
            return nums[0]

        # Recursive helper function
        def linear_layout_dfs(sub_nums):
            memo = {}
            n_sub = len(sub_nums)
            def dfs(i):
                # If we already solved this subproblem (calculated the max amount of money for this house) so reuse result
                if i in memo:
                    return memo[i]
                
                # If i is out of bounds, return 0
                if i >= n_sub:
                    return 0

                # Find which action: skip or rob better to take? 
                skip = dfs(i + 1)
                rob = sub_nums[i] + dfs(i + 2)
                res = max(skip, rob)

                #Store and return max(skip, rob) in memo[i].  
                memo[i] = res
                return res
            return dfs(0)

        # Since we can't rob both the first house and the last house,
        # We can slit the problem into 2 scenarios: 
        # Option 1. Robbing houses from index 0 to n-2 (ignore the last house)
        # Option 2. Robbing houses from index 1 to n-1 (ignore the first house)
        return max(linear_layout_dfs(nums[0:n-1]), linear_layout_dfs(nums[1:n]))