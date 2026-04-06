### OPTIMAL SOLUTION ###

class Solution:
    def isValid(self, s: str) -> bool:
        # Step 1. Create an empty stack 
        stack = []

        # Initialize dict for all bracket pairs 
        pairs = { ")" : "(", "]" : "[", "}" : "{" }

        # Step 2. Loop over every character 
        for char in s:
            # If character is an "opening bracket element"
            if char not in pairs:
                stack.append(char)
            else: 
            # If stack is not empty and last/top "opening bracket" element in the stack matches "closing bracket" element
            # pop that "opening bracket" element 
                if stack and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0