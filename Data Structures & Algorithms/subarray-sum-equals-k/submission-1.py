# Time: O(n) | Space: O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0

        prefix_map = {0: 1}
        prefix_sum = 0

        for num in nums:
            prefix_sum += num

            target = prefix_sum - k
            if target in prefix_map:
                count += prefix_map[target]

            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

        return count