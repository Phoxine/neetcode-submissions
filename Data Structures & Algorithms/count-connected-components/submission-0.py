class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        neighbor_list = [[] for _ in range(n)]
        for edge in edges:
            node1 = edge[0] 
            node2 = edge[1]
            neighbor_list[node1].append(node2)
            neighbor_list[node2].append(node1)
        # print(visited)
        # print(neighbor_list)
        # set all node as visited in connected component
        def dfs(node):
            # print(node)
            if not visited[node]:
                visited[node] = True
                # check neighbor
                for neighbor in neighbor_list[node]:
                    dfs(neighbor)
        count = 0
        for node in range(n):
            if not visited[node]:
                dfs(node)
                count += 1

        return count