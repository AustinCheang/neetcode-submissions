class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if pre_map[crs] == []:
                return True


            visiting.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            pre_map[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True