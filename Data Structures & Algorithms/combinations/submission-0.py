### Backtracking Solution ###

"""
Instead of making include/exclude decisions, we iterate through available numbers and always include one. 
Starting from a given position ensures we never revisit smaller numbers, avoiding duplicates. 
We stop when the combination reaches size k.
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Final answer:
        # This will store all valid combinations of size k
        res = []

        # Backtracking helper function
        # start = the next number we are allowed to use
        # comb  = current combination we are building
        def backtrack(start, comb):

            # Base case:
            # If current combination already has k numbers,
            # we found one valid answer
            if len(comb) == k:
                # Add a COPY of comb into result
                # (important: comb itself will keep changing later)
                res.append(comb.copy())
                return

            # Try every possible next number starting from "start"
            # up to n (inclusive)
            for i in range(start, n + 1):

                # Choose:
                # Add current number i into the combination
                comb.append(i)

                # Explore:
                # Recurse using the next number (i + 1)
                # This prevents reusing the same number
                # and keeps combinations in increasing order
                backtrack(i + 1, comb)

                # Undo choice (Backtrack):
                # Remove the last added number
                # so we can try the next possible number
                comb.pop()

        # Start building combinations from number 1
        backtrack(1, [])

        # Return all valid combinations
        return res


        