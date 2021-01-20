class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        q = collections.deque([tuple(start)])
        visited = set([tuple(start)])
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        while q:
            r, c = q.popleft()
            if r == destination[0] and c == destination[1]:
                return True
            for dx,dy in directions:
                n_r, n_c = r + dx, c + dy
                while 0 <= n_r < len(maze) and 0 <= n_c < len(maze[0]) and maze[n_r][n_c] == 0:
                    n_r += dx
                    n_c += dy
                n_r -= dx
                n_c -= dy
                if (n_r,n_c) not in visited:
                    q.append((n_r,n_c))
                    visited.add((n_r,n_c))
        return False
