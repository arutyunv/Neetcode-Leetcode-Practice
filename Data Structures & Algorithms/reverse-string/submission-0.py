### Two Pointers Approach ### 

"""
The most efficient approach uses two pointers starting at opposite ends of the array. 
We swap the characters at these pointers, then move them toward each other. 
When the pointers meet or cross, every character has been swapped exactly once, and the array is reversed. 
This achieves O(1) space since we only swap in place.
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Initialize left (L) and right (R) pointers 
        L = 0
        R = len(s) - 1
        
        # As long as left pointer not larger (not to the right more) than Right pointer 
        # we change elements in place 
        while L < R:  
            temp = s[L]
            s[L] = s[R]
            s[R] = temp
            L+=1
            R-=1 

        