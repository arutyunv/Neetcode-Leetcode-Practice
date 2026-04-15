### Backtracking Approach ###

# We can build a decision tree, where at each level we make decision of including or not including 
# an element from the array. Leaf level would include all the subsets that do not contain any duplicates. 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # This will store ALL subsets (final answer)
        result_list = [] 
        
        # This stores the CURRENT subset we are building
        subset = []

        # DFS function: explores all choices starting from index i
        def dfs(i):
            # Base case: we have considered all elements
            if i >= len(nums): 
                # We add a COPY of subset, because subset will keep changing
                result_list.append(subset.copy())
                return 

            # Choice 1: INCLUDE nums[i]
            subset.append(nums[i]) # take the element
            dfs(i + 1) # move to next index

            # Choice 2: DO NOT include nums[i]
            subset.pop() # undo the previous choice (backtrack)
            dfs(i + 1) # move to next index

        # Start DFS from index 0
        dfs(0)

        # Return all subsets
        return result_list
