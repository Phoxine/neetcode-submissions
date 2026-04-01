# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node_list = []


        def dfs(node):
            if not node:
                return

            # smaller than current node
            dfs(node.left)
            node_list.append(node)
            # larger than current node
            dfs(node.right)
        dfs(root)
        # start with index 0
        return node_list[k-1].val

