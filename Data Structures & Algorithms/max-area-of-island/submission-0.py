class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        best = 0

        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    area = self._dfs_area(i, j)
                    if area > best:
                        best = area
        return best

    def _dfs_area(self, r: int, c: int) -> int:

        if r < 0 or r >= self.m or c < 0 or c >= self.n or self.grid[r][c] != 1:
            return 0
        self.grid[r][c] = 0

        return 1 + self._dfs_area(r+1, c) + self._dfs_area(r-1, c) \
                 + self._dfs_area(r, c+1) + self._dfs_area(r, c-1)