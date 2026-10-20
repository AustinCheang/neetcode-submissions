class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows, self.cols = len(board), len(board[0])
        self.board = board
        self.word = word

        # Try each cell as a starting point
        for r in range(self.rows):
            for c in range(self.cols):
                if self.dfs(r, c, 0):
                    return True
        return False

    def dfs(self, r: int, c: int, k: int) -> bool:
        # Character mismatch → fail
        if self.board[r][c] != self.word[k]:
            return False
        # Matched last character → success
        if k == len(self.word) - 1:
            return True

        # Mark current cell visited
        temp = self.board[r][c]
        self.board[r][c] = '#'

        # Explore four directions
        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if self.dfs(nr, nc, k + 1):
                    self.board[r][c] = temp
                    return True

        # Backtrack
        self.board[r][c] = temp
        return False