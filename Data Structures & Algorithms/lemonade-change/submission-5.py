class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Keep count for fives and tens 
        five, ten = 0, 0

        # Go over bills 
        for b in bills: 
            # condition 1: if b is 5, then we take it, increment "five" bills and owe no change 
            if b == 5:
                five+=1 
                continue 

            # condition 2: if b is 10, then we take it and need to return $5 change 
            if b == 10:
                # check if we have at least one $5 bill
                if five >= 1:
                    five-=1
                    ten+=1 
                    continue 
                else: 
                    return False 

            # condition 3: if b is 20, then we take it and need to return $15 change giving out 
            # as much $10 as possible 
            if b == 20:
                # check if we have at least one $5 bill and at least $10 bill
                if five >= 1 and ten >= 1:
                    five-=1 
                    ten-=1 
                    continue 
                # else, check if we have at least 3 $5 bills
                elif five >= 3:
                    five-=3
                    continue 
                # else, not possible to give a change 
                else:
                    return False 
                
        return True 

            


        