class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # key: course, value:list[int]
        adjList = collections.defaultdict(list)
        indegree = [0]*numCourses
        
        for course, pre in prerequisites:
            adjList[pre].append(course)
            indegree[course] += 1
        dq = collections.deque()
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                dq.append(i)  # course with 0 degree
        res = []
        while dq:
            i = dq.popleft() # current prerequisite
            res.append(i)
            for course in adjList[i]: # courses
                indegree[course] -= 1 
                if indegree[course] == 0:
                    dq.append(course)
        if sum(indegree) > 0:
            return []
        return res