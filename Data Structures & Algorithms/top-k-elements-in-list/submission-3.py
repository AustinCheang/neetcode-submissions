# Time: O(n + m log k) | Space: O(m)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []

        count = Counter(nums)

        for key, freq in count.items():
            heapq.heappush(min_heap, (freq, key))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [val for _, val in min_heap]