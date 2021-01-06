class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adjDict = collections.defaultdict(set)
        indegree = {char : 0 for word in words for char in word}
        for i in range(len(words) - 1):
            s = words[i]
            t = words[i + 1]   
            
            #["abc","ab"] => invalid order
            if len(s) > len(t) and s[:len(t)] == t:
                return ""
            for j in range(min(len(s),len(t))):
                if s[j] == t[j]:
                    continue
                if t[j] not in adjDict[s[j]]:
                    adjDict[s[j]].add(t[j])
                    indegree[t[j]] += 1 
                break #only compare the front char
        # print(adjDict, indegree)

        dq = collections.deque()
        for key, value in indegree.items():
            if value == 0:
                dq.append(key)
        
        res = []
        while dq:
            cur_node = dq.popleft()
            res.append(cur_node)
            for child in adjDict[cur_node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    dq.append(child)
        # print (res)
        if len(res) != len(indegree):
            return ""
        else:
            return "".join(res)