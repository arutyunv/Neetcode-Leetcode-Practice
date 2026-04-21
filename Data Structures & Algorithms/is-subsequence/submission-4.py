### Two-Pointers Approach ###

"""

One pointer loop over the first string and second pointer loops over the second string. 


"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True 

        pointer1 = 0
        pointer2 = 0 
        subsequence = ""

        for pointer1 in range(len(t)): 
            if t[pointer1] == s[pointer2]:
                subsequence += s[pointer2]
                pointer2+=1 
            
            if subsequence == s:
                return True 
        
        return False 
        
    