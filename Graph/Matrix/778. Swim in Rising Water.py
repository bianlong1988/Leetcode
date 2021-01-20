class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # min path - dijkstra
        # BFS + heap => update the min time at each step
        n = len(grid)
        pq = []
        heapq.heappush(pq, (grid[0][0], 0, 0)) # (time, r, c)
        visited = set((0, 0))
        directions = [(-1,0), (1,0), (0, 1), (0, -1)]
        res = 0
        while pq:
            t, r, c = heapq.heappop(pq)
            if r == n - 1 and c == n - 1:
                return t
            for dx, dy in directions:
                x, y = r + dx, c + dy
                if 0 <= x <= n -1 and 0 <= y <= n -1 and (x,y) not in visited:
                    max_t = max(t, grid[x][y])
                    heapq.heappush(pq, (max_t, x, y)) # inherit the max weight on each node
                    visited.add((x,y))
                                   
                
        
