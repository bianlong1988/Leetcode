class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        #construct graph
        values = {val for seq in seqs for val in seq}
        graph = {x: [] for x in values}
        indegrees = {x: 0 for x in values}
        for seq in seqs:
            for i in range(len(seq) - 1):
                s = seq[i]
                t = seq[i + 1]
                graph[s].append(t)
                indegrees[t] += 1
        dq = collections.deque()
        
        for node, count in indegrees.items():
            if count == 0:
                dq.append(node)
        res = []   
        while dq:
            if len(dq) != 1: # not unique
                return False
            i = dq.popleft()
            res.append(i)
            for node in graph[i]:
                indegrees[node] -= 1
                if indegrees[node] == 0:
                    dq.append(node)
        return len(res) == len(values) and res == org
            
            