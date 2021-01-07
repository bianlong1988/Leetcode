class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjDict = collections.defaultdict(list)
        preSet = collections.defaultdict(set)
        inDegree = {i: 0 for i in range(n)}
        for pre, nxt in prerequisites:
            adjDict[pre].append(nxt)
            inDegree[nxt] += 1
            preSet[nxt].add(pre)
        # print (adjDict, inDegree, preSet)
        
        dq = collections.deque()
        for key, degree in inDegree.items():
            # print (key, degree)
            if degree == 0:
                dq.append(key)
        while dq:
            pre = dq.popleft()
            # print (pre, adjDict[pre])
            for nxt in adjDict[pre]: # 0-> 1 ->[2,3,4]
                                   #       pre -> nxt
                # set union:  (preSet[nxt]) U (pre's ancestors)
                preSet[nxt] = preSet[nxt] | preSet[pre]  
                inDegree[nxt] -= 1
                if inDegree[nxt] == 0:
                    dq.append(nxt)
        # print (preSet)
        res = []
        for pre, nxt in queries:
            if pre in preSet[nxt]:
                res.append(True)
            else:
                res.append(False)
        return res