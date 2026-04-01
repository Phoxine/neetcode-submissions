# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.solveWithBFS(root)

    
    def solveWithDFS(self, root):
        pass
    def solveWithBFS(self, root):
        if not root:
            return []

        from collections import deque

        queue = deque()
        queue.append(root)
        node_list = []
        while queue:
            node_count = len(queue)
            layer_node_list = []
            for i in range(node_count):
                node = queue.popleft()
                layer_node_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            node_list.append(layer_node_list)
        return node_list
        
