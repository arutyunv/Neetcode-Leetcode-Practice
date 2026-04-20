### Brute Force ###

"""
To check if a string is a palindrome, we only care about letters and digits - everything else can be ignored. 
We can build a cleaned version of the string that contains only alphanumeric characters, all converted to lowercase for consistency. 
Once we have this cleaned string, the problem becomes very simple: a string is a palindrome if it is exactly the same as in reverse.  
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create an empty string to store only valid characters
        newStr = ''
        
        # Go through each character in the original string
        for char in s:
            
            # Check if the character is a letter or digit
            # (ignore spaces, punctuation, etc.)
            if char.isalnum():
                
                # Convert it to lowercase and add to newStr
                # This ensures case doesn't matter (A == a)
                newStr += char.lower()
        
        # Compare the cleaned string with its reversed version
        # [::-1] means "reverse the string"
        return newStr == newStr[::-1]

        