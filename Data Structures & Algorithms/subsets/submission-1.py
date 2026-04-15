### Iteration Approach ###

# Start with just one subset: the empty set [], for every number in the array, we take all
# the subsets we have so far and create new subsets by adding the current number to each of them. 


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Start with one subset: the empty subset
        res = [[]]

        # Go through each number in the input
        for num in nums:
            # For every existing subset in res,
            # create a NEW subset that includes current num
            # subset + [num] - makes a new list (does NOT modify original)
            # Then we ADD these new subsets to res
            res += [subset + [num] for subset in res]

        # After processing all numbers, res contains ALL subsets
        return res
        