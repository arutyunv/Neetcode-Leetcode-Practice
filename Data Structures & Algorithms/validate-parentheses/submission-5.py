### OPTIMAL SOLUTION ###

class Solution:
    def isValid(self, s: str) -> bool:
        # Step 1. Create an empty stack; stack collects "opening" brackets
        stack = []

        # Initialize dict for all bracket pairs 
        pairs = { ")" : "(", "]" : "[", "}" : "{" }

        # Step 2. Loop over every character 
        for char in s:
            # If character is an "opening bracket element"
            if char not in pairs:
                stack.append(char)
            else: 
            # If char is closing bracket element
            # Check if stack is not empty and last/top "opening bracket" element in the stack matches the currect closing bracket
            # If there is a match, pop/remove that "opening bracket" element 
                if stack and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    # if stack is empty OR there is no match happened
                    return False

        # At the end, check if stack is empty
        return len(stack) == 0