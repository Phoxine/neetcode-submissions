# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
        
        if self.same(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def same(self, node_a, node_b):
        
        if not node_a and not node_b:
            return True

        # one node exists
        if not node_a or not node_b:
            return False

        if node_a.val != node_b.val:
            return False

        return self.same(node_a.left, node_b.left) and self.same(node_a.right, node_b.right)

            