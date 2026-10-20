class Solution:
    # Time: O(1) | Space: O(1)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # step 1: row-wise checking
        for row in range(9):
            if not self._is_valid_unit(board[row][col] for col in range(9)):
                return False

        # step 2: colume-wise checking
        for col in range(9):
            if not self._is_valid_unit(board[row][col] for row in range(9)):
                return False

        # step 3: 3x3 box checking
        for box_row in range(3):
            for box_col in range(3):
                box_cells = []
                for i in range(3):
                    for j in range(3):
                        row = box_row * 3 + i
                        col = box_col * 3 + j
                        box_cells.append(board[row][col])
                if not self._is_valid_unit(box_cells):
                    return False
        return True

    def _is_valid_unit(self, cells: List[str]) -> bool:
        seen = set()
        for cell in cells:
            if cell != "." and cell in seen:
                return False
            seen.add(cell)
        return True

            