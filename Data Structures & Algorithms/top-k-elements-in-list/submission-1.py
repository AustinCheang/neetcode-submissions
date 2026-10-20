class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        count = Counter(nums)
        for num, freq in count.items():
            heapq.heappush(heap, [-freq, num])

        result = []
        for _ in range(k):
            c, val = heapq.heappop(heap)
            result.append(val)

        return result