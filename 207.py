from typing import DefaultDict


# class Solution:
#     def canFinish(self, numCourses: int, prerequisites) -> bool:

        ### backtracking 
    #     visited = set()
    #     courseDict = {i:[] for i in range(numCourses)}
    #     for course,prereq in prerequisites: 
    #         courseDict[course].append(prereq)

    #     def isCycle(course):
    #         if course in visited: 
    #             return True 
    #         if not courseDict[course]: 
    #             return False 
    #         visited.add(course)
    #         ret=False
    #         for child in courseDict[course]: 
    #             ret =  isCycle(child)
    #             if ret: 
    #                 break 
    #         visited.remove(course)
    #         return ret 

    #     for course in range(numCourses): 
    #         if isCycle(course): 
    #             return False 
    #     return True
    # 

        # ## dfs
        # visited = set()
        # courseDict = {i:[] for i in range(numCourses)}
        # for course,prereq in prerequisites: 
        #     courseDict[course].append(prereq)

        # def dfs(course): 
        #     if course in visited: 
        #         return False
        #     if not courseDict[course] :
        #         return True
        #     visited.add(course)
        #     for neighbor in courseDict[course]: 
        #         if not dfs(neighbor): 
        #             return False
        #     visited.remove(course)
        #     courseDict[course] = []
        #     return True 

        # for course in range(numCourses): 
        #     if not dfs(course): 
        #         return False
        # return True


        ### top sort

class GNode(object):
    """  data structure represent a vertex in the graph."""
    def __init__(self):
        self.inDegrees = 0
        self.outNodes = []

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict, deque
        # key: index of node; value: GNode
        graph = defaultdict(GNode)

        totalDeps = 0
        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            graph[prevCourse].outNodes.append(nextCourse)
            graph[nextCourse].inDegrees += 1
            totalDeps += 1

        # we start from courses that have no prerequisites.
        # we could use either set, stack or queue to keep track of courses with no dependence.
        nodepCourses = deque()
        for index, node in graph.items():
            if node.inDegrees == 0:
                nodepCourses.append(index)

        removedEdges = 0
        while nodepCourses:
            # pop out course without dependency
            course = nodepCourses.pop()

            # remove its outgoing edges one by one
            for nextCourse in graph[course].outNodes:
                graph[nextCourse].inDegrees -= 1
                removedEdges += 1
                # while removing edges, we might discover new courses with prerequisites removed, i.e. new courses without prerequisites.
                if graph[nextCourse].inDegrees == 0:
                    nodepCourses.append(nextCourse)

        if removedEdges == totalDeps:
            return True
        else:
            # if there are still some edges left, then there exist some cycles
            # Due to the dead-lock (dependencies), we cannot remove the cyclic edges
            return False


inp =  [[1,0],[0,1]]
solution = Solution()
res = solution.canFinish(2,inp)
print(res)
            

        
        
