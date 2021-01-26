class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        pq = []
        heapq.heappush(pq,(0, start[0],start[1]))
        dist = {(start[0],start[1]):0}
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while pq:
            d, r, c = heapq.heappop(pq)
            if [r, c] == destination:
                return d
            # print (r,c, steps)
            # print (dist)            
            for dx, dy in directions:
                n_r, n_c, steps = dx + r, dy + c, 1  # set step to 1 instead of 0
                # print ("cur", (n_r, n_c, d + steps))
                while 0<=n_r<len(maze) and 0<=n_c<len(maze[0]) and maze[n_r][n_c] == 0:
                    n_r += dx
                    n_c += dy
                    steps += 1
                    # print ("next", (n_r, n_c, d + steps))
                n_r -= dx
                n_c -= dy
                steps -= 1
                # print ((n_r, n_c, d + steps))
                if (n_r, n_c) not in dist or d + steps < dist[(n_r, n_c)]:
                    # print ((n_r, n_c, d + steps))
                    heapq.heappush(pq, (d + steps, n_r, n_c))
                    dist[(n_r, n_c)] = d + steps
        return -1
                    