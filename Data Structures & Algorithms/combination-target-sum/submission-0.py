### Backtracking Approach ###

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # This will store ALL valid combinations
        res = [] 
        
        # This will store the CURRENT combination we are building
        curr = [] 

        # DFS function:
        # i: current index in nums we are considering
        # curr: current combination (list of chosen numbers)
        # total: current sum of elements in curr
        def dfs(i, curr, total): 
            
            # Base case 1: we hit target
            if total == target:
                # Found a valid combination!
                # We append a COPY because curr will change later
                res.append(curr.copy())
                return 

            # Base case 2: invalid path
            # - i is out of bounds: no more numbers to use
            # - total exceeded target: no need to continue
            if i >= len(nums) or total > target:
                return 

            # Decision 1: INCLUDE nums[i]
            # Add nums[i] to current combination
            curr.append(nums[i])

            # Stay at same index i
            # WHY? Because we can reuse the same number multiple times
            dfs(i, curr, total + nums[i])

            # BACKTRACK
            # Undo the previous decision
            curr.pop()

            # Decision 2: SKIP nums[i]
            # Move to next index (i + 1)
            dfs(i + 1, curr, total)

        # Start DFS:
        # - index = 0 (start from first number)
        # - curr = empty combination
        # - total = 0 (no sum yet)
        dfs(0, [], 0)

        # Return all valid combinations
        return res
