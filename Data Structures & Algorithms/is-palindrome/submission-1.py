### Two Pointer Algorithms ###

"""
Palindrome string is a string that is read the same from the start as well as from the end, therefore we can use two pointers (L and R) 
and check if two mirrored-opposite elements match (L=0 and R=arr.length-1, L = 1 and R=arr.length-2)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointers: one at the start, one at the end
        l, r = 0, len(s) - 1

        # Keep checking while pointers haven't crossed
        while l < r:

            # Move left pointer until we find a letter or digit
            while l < r and not self.alphaNum(s[l]):
                l += 1

            # Move right pointer until we find a letter or digit
            while l < r and not self.alphaNum(s[r]):
                r -= 1

            # Compare characters (ignore case)
            if s[l].lower() != s[r].lower():
                return False  # not a palindrome

            # Move both pointers inward
            l += 1
            r -= 1

        # If we never found a mismatch so it's a palindrome
        return True

    def alphaNum(self, c):
        # Check if character is a letter (A-Z, a-z) or digit (0-9)
        return (
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')
        )