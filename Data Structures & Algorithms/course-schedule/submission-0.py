class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create a map 
        courseMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites: 
            courseMap[crs].append(pre)

        path = set() 

        def dfs(course): 
            preq = courseMap[course]

            if course in path: 
                return False # cycle 
            
            if preq == []: 
                return True 

            path.add(course)
            for pre in preq: 
                if not dfs(pre): return False 
            
            path.remove(course)
            courseMap[course] = []

            return True 
        
        for c in range(numCourses): 
            if not dfs(c): return False 
        
        return True 

        