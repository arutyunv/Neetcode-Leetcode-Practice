### OPTIMAL SOLUTION W/ SUFFIX MAX PATTERN ### 

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Step 1. Initialize array ans that will be populated and returned 
        ans = [0] * len(arr)

        # Step 2. Initialize rightMax to -1 (means there is no values to the right)
        rightMax = -1 

        # Step 3. loop over from end/right to the front/left of array 
        for i in range(len(arr)-1, -1, -1): 
            ans[i] = rightMax
            rightMax = max(arr[i], rightMax)
        
        return ans

