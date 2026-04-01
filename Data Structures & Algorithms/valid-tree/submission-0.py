class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        node_list = [[] for _ in range(n)]
        visited = set()
        for x, y in edges:
            node_list[x].append(y)
            node_list[y].append(x)

        def dfs(node, parent_node):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in node_list[node]:
                if neighbor == parent_node:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
        # check all node visited
        return dfs(0, -1) and len(visited) == n

            