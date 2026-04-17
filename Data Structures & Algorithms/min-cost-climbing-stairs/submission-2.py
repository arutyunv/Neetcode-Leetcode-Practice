### Recursive (DFS) Approach w/o memoization ###

"""
From any step, you can climb 1 or 2 steps.
If you step on index i, you must pay cost[i], then choose the cheaper path ahead.
So the problem is: from each step, pick the minimum cost path to the top.
"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # dfs(i) = minimum cost to reach the top starting from step i
        def dfs(i):
            # Base case:
            # If we go beyond the last step, we’ve reached the top
            # no more cost to pay
            if i >= len(cost):
                return 0
            
            # At step i, we have two choices:
            # 1. Take 1 step so go to i + 1
            # 2. Take 2 steps so go to i + 2
            # We choose the option with minimum total cost
            return cost[i] + min(dfs(i + 1), dfs(i + 2))

        # We can start either from step 0 or step 1
        # Return the minimum cost of both starting points
        return min(dfs(0), dfs(1))

