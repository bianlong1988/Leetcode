class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = collections.deque([start])
        visited = set([start])
        # visited.add(start)
        while q:
            i = q.popleft()
            if arr[i] == 0:
                return True
            for new_i in [i + arr[i], i - arr[i]]:
                if 0 <= new_i <= len(arr) - 1 and new_i not in visited:
                    q.append(new_i)
                    visited.add(new_i)
            
        return False