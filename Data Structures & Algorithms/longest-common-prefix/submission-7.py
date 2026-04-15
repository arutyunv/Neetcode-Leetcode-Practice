### Vertical Scanning ### 

## Idea: Instead of comparing horizontally, we can compare characters column by column across all strings. 
# Check if all strings have the same character at position 0, then position 1. 
# The moment we find a mismatch or reach the end of any string, we have found where 
# the common prefix ends. 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Find min length string 
        min = 201
        for string in strs:
            if len(string) < min:
                min = len(string)
                min_string = string 
        
        prefix = ""
        # Looping over strings in the array 
        for j in range(len(min_string)):
            for i in range(len(strs)): 
                if strs[i][j] != min_string[j]:
                    return prefix 
            prefix += min_string[j]

        return prefix
            


        