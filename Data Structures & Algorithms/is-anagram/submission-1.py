### Brute force ###

# Idea: Sort given strings and check for their equality 
# Runtime: O(nlogn + mlogm), where n - length of the first string s 
# and m - length of the second string t 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check an edge case: if length of string s is not the same as length of string t 
        # they can't be anagrams 
        if len(s) != len(t):
            return False 

        # note: sorted(nums)
        # standalone Python function
        # works on any iterable (lists, tuples, etc.)
        # returns a new sorted list   
        return sorted(s) == sorted(t)
        