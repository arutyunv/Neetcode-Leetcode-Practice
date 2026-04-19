### Brute Force Solution ### 

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # Loop over each index L (left pointer)
        for L in range(len(nums)):
            
            # Set R pointer (Right pointer)
            # Check the next k elements AFTER L
            # We go up to L + k (inclusive), so we use L + k + 1 in range
            for R in range(L + 1, min(L + k + 1, len(nums))):
                
                # If we find the same value within distance k → return True
                # Note: abs(L - R) <= k is ALWAYS true here because R ≤ L + k
                if nums[L] == nums[R]:
                    return True 

        # If no such pair found
        return False
        