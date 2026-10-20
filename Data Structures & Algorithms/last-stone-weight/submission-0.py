class Solution:
    # Time: O(n log n) | Space: O(n)
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [ -x for x in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            heapq.heappush(heap, - (x - y))

        return -heap[0] if heap else 0