### This is recursion case w/o memoization ### 

"""
Since we use no memoization, we need to compute dfs(x) for each node. 
This is exponential because each call branches into two, forming a binary recursion tree of height n and total nodes is O(2^n).

Example) 
Level 0 → 1 node
Level 1 → 2 nodes
Level 2 → 4 nodes
Level 3 → 8 nodes
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        
        # dfs(x) = number of ways to climb x remaining steps
        def dfs(remaining_steps: int) -> int:
            
            # Base case: exactly reached the top
            if remaining_steps == 0:
                return 1
            
            # Base case: overshot the top
            if remaining_steps < 0:
                return 0
            
            # Try taking 1 step or 2 steps
            return dfs(remaining_steps - 1) + dfs(remaining_steps - 2)
        
        # Start with n steps remaining
        return dfs(n)
