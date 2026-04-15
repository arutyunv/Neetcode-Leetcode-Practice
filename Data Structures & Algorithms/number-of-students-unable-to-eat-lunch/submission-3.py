### Frequency Count Approach ### 

# Idea: The key insight is that student order does NOT matter.
# Even though students stand in a queue, they can rotate forever.
# So instead of simulating the queue, we only care:
# "Do we have ANY student who wants this sandwich?"

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        # Initially, ALL students are hungry
        # We will decrease this number whenever a student successfully eats
        hungry_students = len(students)

        # Dictionary to count how many students want each type of sandwich
        # Example: {0: 3, 1: 2}
        # Meaning:
        #   3 students want sandwich type 0
        #   2 students want sandwich type 1
        cnt = {0: 0, 1: 0}

        # Build the frequency map
        for student in students: 
            # Increment the count for this sandwich type
            cnt[student] += 1

        # Now we go through sandwiches in STACK order (top to bottom)
        for s in sandwiches: 
            
            # Check: is there ANY student who wants this sandwich?
            if cnt[s] > 0:
                
                # One student takes the sandwich → one less hungry student
                hungry_students -= 1
                
                # Decrease the count of students who want this type
                cnt[s] -= 1
            
            else:
                # If NO student wants this sandwich,
                # then nobody will ever take it (even after infinite rotations)
                # So we STOP immediately
                break 
        
        # Return how many students are still hungry
        return hungry_students
