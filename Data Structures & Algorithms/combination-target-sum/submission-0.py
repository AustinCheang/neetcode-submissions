class Solution:
    # Time: O(n log n) | Space: O(target / min(nums))
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        path = []
        self.backtracking(nums, target, 0, 0, path, result)
        return result

    def backtracking(self, nums, target, start_idx, curr_sum, path, result):
        if curr_sum == target:
            result.append(path.copy())
            return

        for i in range(start_idx, len(nums)):
            new_val = nums[i]

            if curr_sum + new_val > target:
                return

            path.append(new_val)
            self.backtracking(nums, target, i, curr_sum + new_val, path, result)
            path.pop()
