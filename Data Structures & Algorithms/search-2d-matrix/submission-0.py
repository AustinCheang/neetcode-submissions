class Solution:
    # Time: O(log(m*n)) | Space: O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix[0]) == 0:
            return False

        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            mid = left + (right - left) // 2

            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False