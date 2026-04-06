### BRUTE FORCE SOLUTION ###

class Solution:
    def isValid(self, s: str) -> bool:
        # Check if we have a valid open-close bracket pair 
        while '()' in s or '{}' in s or '[]' in s:
            # If we found a pair, we remove it 
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        
        # Check if something was not removed (invalid soltion - return False) or everuthing was removed (valid soltion - return True)
        return s == ''