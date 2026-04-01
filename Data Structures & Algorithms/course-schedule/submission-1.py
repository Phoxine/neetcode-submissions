from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        course_prerequisite = defaultdict(list)
        indegree = [0] * numCourses
        queue = deque()
        for a, b in prerequisites:
            indegree[b] += 1
            course_prerequisite[a].append(b)

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        courses_to_take = 0
        while queue:
            node = queue.popleft()
            courses_to_take += 1
            for neighbor in course_prerequisite[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)


        return courses_to_take == numCourses