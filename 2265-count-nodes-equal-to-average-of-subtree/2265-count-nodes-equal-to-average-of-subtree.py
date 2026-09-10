# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0

        def dfs(node):
            nonlocal count

            if node is None:
                return 0, 0

            # Get sum and count from left subtree
            left_sum, left_count = dfs(node.left)

            # Get sum and count from right subtree
            right_sum, right_count = dfs(node.right)

            # Sum and count of current node's entire subtree
            total_sum = node.val + left_sum + right_sum
            total_count = 1 + left_count + right_count

            # Check average
            if node.val == total_sum // total_count:
                count += 1

            return total_sum, total_count

        dfs(root)

        return count
        