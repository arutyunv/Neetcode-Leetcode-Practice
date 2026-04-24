### Dynamic Programming (Top-Down) Using Hash Set ###

"""
The recursive solution has overlapping subproblems since we may compute the answer for the same index multiple times. Memoization stores results so each subproblem is solved only once.

Using a hash set for the dictionary allows efficient substring lookups. 
The memoization table dp[i] stores the minimum extra characters from index i onward.
"""

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        # Convert dictionary list → set for O(1) lookup
        words = set(dictionary)
        
        # Memoization cache:
        # key = index i
        # value = minimum extra characters starting from i
        cache = {}

        # DFS function: returns minimum extra chars from index i → end
        def dfs(i):
            
            # Base case:
            # If we reached the end of the string → no extra characters left
            if i == len(s): 
                return 0 

            # If already computed → reuse result (IMPORTANT optimization)
            if i in cache:
                return cache[i]

            # Option 1: Treat current character as "extra"
            # So we skip it and add +1 penalty
            res = 1 + dfs(i+1)

            # Option 2: Try matching substrings starting at index i
            for j in range(i, len(s)):
                
                # If substring s[i : j+1] exists in dictionary
                if s[i:j+1] in words: 
                    
                    # No penalty for this substring
                    # Jump directly to j+1
                    res = min(dfs(j+1), res)
                
            # Store result in cache to avoid recomputation
            cache[i] = res
            
            # Return the best result for index i
            return res 

        # Start DFS from index 0
        return dfs(0)

        