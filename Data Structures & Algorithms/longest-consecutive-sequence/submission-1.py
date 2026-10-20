# Time: O(n) | Space: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                curr = num

                while curr in nums_set:
                    curr += 1

                max_len = max(max_len, curr - num)

        return max_len