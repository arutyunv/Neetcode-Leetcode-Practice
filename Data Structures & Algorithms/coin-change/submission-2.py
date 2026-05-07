### Recursive Approach ### 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # Define memo
        memo = {}

        def recursive_helper(left_amount): 

            # Store the best (minimum) answer found so far
            best = float('inf')

            # If left_amount in memo, just return it 
            if left_amount in memo:
                return memo[left_amount]

            # If remaining amount becomes 0,
            # we successfully formed the target
            # and need 0 more coins
            if left_amount == 0:
                return 0

            # If remaining amount becomes negative,
            # this path is invalid
            if left_amount < 0: 
                return float('inf')

            # Try every coin
            for i in range(len(coins)): 

                # Recursive case:
                # choose coin coins[i]
                # and solve smaller subproblem
                if left_amount >= coins[i]:

                    # Solve for the remaining amount
                    result = recursive_helper(left_amount - coins[i])

                    # If recursive call returned a valid answer
                    if result != float('inf'):

                        # +1 because we used one coin: coins[i]
                        best = min(best, result + 1)

            # Save to the memo 
            memo[left_amount] = best 

            # Return the minimum coins found
            return best 

        # Start recursion from full target amount
        answer = recursive_helper(amount)

        # If answer is still infinity,
        # it means no solution exists
        return -1 if answer == float('inf') else answer