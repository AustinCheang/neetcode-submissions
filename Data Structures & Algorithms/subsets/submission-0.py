class Solution:
    # Time: (2^n * n) | Space: O(n) 
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        self.backtracking(nums, 0, path, result)
        return result

    def backtracking(self, nums: List[int], start_idx: int, path: List[int], result: List[List[int]]) -> None:
        result.append(path[:])

        for i in range(start_idx, len(nums)):
            path.append(nums[i])
            self.backtracking(nums, i + 1, path, result)
            path.pop()
        