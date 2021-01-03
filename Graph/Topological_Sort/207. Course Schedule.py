class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dictionary key: prerequisite; value: [courses] 
        # {1:[2,4]}
        # 1 ---->2
        #  \---->4  
        adjDict = collections.defaultdict(list)
        # build an indegree list [0, 0, 1 ....]
        indegree = [0]*numCourses
        for course, pre in prerequisites:
            adjDict[pre].append(course)
            indegree[course] += 1
        # add 0 degree elemnts in dq
        dq = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                dq.append(i)
        # BFS
        while dq:
            i = dq.popleft()
            for node in adjDict[i]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    dq.append(node)
        # if there any indegree not 0, has cycle
        return not sum(indegree)
        
        
            

            

