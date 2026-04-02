#### TWO PASS (BRUTE FORCE) SOLUTION #### 

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Step 1. Initialize array ans that will be returned
        ans = [] 

        # Step 2. Loop for 2 iterations over array nums 
        for i in range(2):
            # go over each element in array nums and append it to ans array 
            for num in nums:
                ans.append(num)

        return ans 