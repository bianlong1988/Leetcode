class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict((list))
        pq = [(0, k)]
        dist = {}
        for s, d, t in times: # source, destination, arrival time
            graph[s].append((d, t))
        # print (graph)
        while pq:
            cur_t, cur = heapq.heappop(pq)
            if cur in dist:   # if node in the distance dictionary
                continue  # no need to upodate the node in the dic, since BFS + heap garantee shortest path
            dist[cur] = cur_t
            for nxt, nxt_t in graph[cur]:
                if nxt not in dist:
                    heapq.heappush(pq, (cur_t + nxt_t, nxt))
        print (dist)
        return max(dist.values()) if len(dist) == n else -1
                
                