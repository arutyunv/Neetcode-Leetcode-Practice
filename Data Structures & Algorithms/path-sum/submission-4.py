### Depth First Search - Iterative approach ###

## Simulate the recursive dfs using an explicit stack
## Each stack entry stores a node and the remaining sum 
## needed to reach the target from that node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # If the tree is empty, there cannot be any root-to-leaf path,
        # so return False right away.
        if not root:
            return False 


        # We use a stack for iterative DFS.
        # Each item in the stack is a pair:
        # (current node, remaining sum after using this node's value)
        #
        # Since we start at the root, we subtract root.val from targetSum.
        # That tells us how much sum is still needed.
        stack = [(root, targetSum - root.val)]
        # Keep going while there are still nodes to process.
        while stack:
            # Pop the top item from the stack.
            # This gives us:
            # - node: the current tree node we are visiting
            # - curr_sum: how much sum is still needed for this path
            node, curr_sum = stack.pop()

            # Check if this node is a leaf:
            # - no left child
            # - no right child
            # And also check whether the remaining sum is exactly 0.
            #
            # If yes, then the path from root to this leaf adds up to targetSum.
            if not node.left and not node.right and curr_sum == 0:
                return True

            # If there is a right child,
            # push it onto the stack.
            #
            # For that child, we update the remaining sum by subtracting
            # the child's value, because we are now including that child
            # in the path.
            if node.right:
                stack.append((node.right, curr_sum - node.right.val))

            # If there is a left child,
            # push it onto the stack too.
            #
            # Again, subtract the left child's value from the remaining sum
            # because that child becomes part of the path.
            if node.left:
                stack.append((node.left, curr_sum - node.left.val))

        # If we finish the whole DFS and never find a valid path,
        # return False.
        return False  