class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = {} # not visited
        for node in range(n):
            # if visited[i]:
            #     continue
            if node not in visited:
                dq = collections.deque([node])
                visited[node] = 0 # set group to arbitary 0 or 1
                while dq:
                    cur_node = dq.pop()
                    for nei in graph[cur_node]:
                        if nei not in visited:
                            dq.append(nei)
                            visited[nei] = visited[cur_node] ^ 1  # 0^1, 1^1 => xor
                        elif visited[nei] == visited[cur_node]: # check group
                            return False
        return True