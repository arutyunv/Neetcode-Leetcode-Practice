class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # This set will store the elements inside the current sliding window
        window = set()
        
        # Left pointer of the window (start of the window)
        L = 0 

        # R is the right pointer so we expand the window to the right
        for R in range(len(nums)):
            
            # If window size becomes larger than k
            # (distance between L and R exceeds k)
            if R - L > k:
                # Remove the leftmost element from the set
                # because it's no longer in the allowed window
                window.remove(nums[L])
                
                # Move left pointer forward to shrink window
                L += 1
            
            # Check if current element already exists in the window
            # If yes so we found duplicate within distance ≤ k
            if nums[R] in window:
                return True 
            
            # Add current element to the window
            window.add(nums[R])

        # If no duplicates found within distance k
        return False
        