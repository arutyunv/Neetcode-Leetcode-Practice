### Two-Pointer Approach ###

"""
Merge two strings by alternating their characters.

We use two pointers:
- pointer1 so tracks position in word1
- pointer2 so tracks position in word2

At each step, we add one character from each word.
When one word runs out, we append the remaining part
of the longer word.
 """

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # This will store the final merged string
        new_string = ''

        # Determine which word is shorter and which is longer
        # (used later to append leftover characters)
        if len(word1) >= len(word2):
            shortest = word2
            longest = word1
        else:
            shortest = word1 
            longest = word2

        # Initialize two pointers for both words
        pointer1 = 0
        pointer2 = 0 

        # Loop through the length of the shorter word
        # because after that, one word will be exhausted
        for i in range(len(shortest)):

            # Add one character from word1
            new_string += word1[pointer1]

            # Add one character from word2
            new_string += word2[pointer2]

            # Move both pointers forward
            pointer1 += 1
            pointer2 += 1 

        # After the loop, one word may still have characters left
        # Append the remaining part of the longer word
        new_string += longest[len(shortest):]

        # Return the final merged string
        return new_string
