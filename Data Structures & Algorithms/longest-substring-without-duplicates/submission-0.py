### Brute Force Approach ###

"""
We try the substring starting at index i and try to find the maximum length we can form 
without duplicates by starting at that index.

Use HashSet to detect duplicates in O(1) time 


"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Edge case: check if the string is empty
        # Is string is empty, we need to return 0 
        if not s:
            return 0

        # Keeping track of max length string 
        maxLength = 0

        # Go over every index in string s 
        for i in range(len(s)):

            # Initialize HashSet seen to track the characters from the current substring 
            seen = set()

            # Creating longer and longer substrings 
            # And checking if we have duplicates in the substring 
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
                maxLength = max(maxLength, j - i + 1)

        return maxLength
                

        