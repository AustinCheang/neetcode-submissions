class Solution:
    # Time: (mn) | Space: O(mn)
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self._flood_fill_dfs(grid, i, j)
        return count

    def _flood_fill_dfs(self, grid: List[List[str]], i: int, j: int) -> None:
        m, n = len(grid), len(grid[0])
        stack = [(i, j)]
        grid[i][j] = '2'
        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while stack:
            r, c = stack.pop()
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                    grid[nr][nc] = '2'
                    stack.append((nr, nc))
