### Two-Pointers Approach ###

"""
We use two pointers:
    One pointer (pointer1) goes through string t (the big string)
    One pointer (pointer2) tracks progress in string s (the subsequence we are trying to match)

Idea:
    We scan t and try to match characters of s in order.
    If we manage to match all characters of s, then s is a subsequence of t.
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # If s is empty, it's always a subsequence
        if s == "":
            return True
        
        # Pointer for string s (what we want to match)
        j = 0
        
        # Loop through string t (the bigger string)
        for i in range(len(t)):
            
            # If current characters match
            if t[i] == s[j]:
                # Move pointer in s forward (we matched one char)
                j += 1
            
            # If we matched all characters of s
            if j == len(s):
                return True
        
        # If we finish looping and didn't match all of s
        return False
        
    