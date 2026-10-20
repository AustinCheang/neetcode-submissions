class Solution:
    # Time: O(2^n) | Space: O(n log n)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        path = []

        self.backtracking(nums, 0, path, result)
        return result

    def backtracking(self, nums, start_idx, path, result):
        result.append(path.copy())

        for i in range(start_idx, len(nums)):
            if i > start_idx and nums[i] == nums[i - 1]:
                continue

            path.append(nums[i])

            self.backtracking(nums, i + 1, path, result)

            path.pop()