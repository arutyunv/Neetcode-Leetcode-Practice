### Dynamic Programming (Top-Down) ### 

"""
We can visualize this problem as building a decision tree. We have n steps at the beginning, so we have two choices,
take 1 step or two steps, then go deeper, and from that choice of taking 1 step, we can also make two choices: take 2 steps or 1 step. 

        n
      /   \
   n-1     n-2
  /  \     /  \
...  ...  ... ...

This recursion: dfs(n) = dfs(n-1) + dfs(n-2)
builds a decision tree where at each step you choose:
 * take 1 step
 * take 2 steps

Without memoization, we might need to compute, for example, dfs(3) multiple times in the tree. With memoization, we can compute 
compute once, reuse result later when needed. 

This is TOP-DOWN approach, because we start from the final problem: dfs(n)
Then break it into smaller ones: dfs(n-1), dfs(n-2) (you go from big to small) -> Top-down = recursion + memoization

Complexity 

Time: O(n) (each state computed once)
Space: O(n) (memo + recursion stack)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # Dictionary to store already computed results
        # key = remaining steps, value = number of ways
        memo = {}

        # Recursive helper function
        # remaining_steps = how many steps we still need to climb
        def dfs(remaining_steps: int) -> int:

            # If we already solved this subproblem so reuse result
            if remaining_steps in memo:
                return memo[remaining_steps]

            # Base case 1:
            # Exactly reached the top so 1 valid way
            if remaining_steps == 0:
                res = 1

            # Base case 2:
            # Went past the top so invalid path so 0 ways
            elif remaining_steps < 0:
                res = 0

            # Recursive case:
            # Try taking 1 step OR 2 steps
            else:
                res = dfs(remaining_steps - 1) + dfs(remaining_steps - 2)

            # Store result in memo to avoid recomputation
            memo[remaining_steps] = res

            # Return number of ways for this state
            return res

        # Start recursion from n steps
        return dfs(n)
