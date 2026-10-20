class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        freq = Counter(tasks)
        max_heap = [-cnt for cnt in freq.values()]
        heapq.heapify(max_heap)

        time = 0
        cooldown = deque()  # [(ready_time, neg_remaining), ...]

        while max_heap or cooldown:
            # Phase 0: 若堆空且下一個可執行時間在未來 → 跳時
            if not max_heap and cooldown and cooldown[0][0] > time:
                time = cooldown[0][0]

            # Phase 1: 釋放所有已冷卻完成的任務回堆
            while cooldown and cooldown[0][0] <= time:
                _, neg_rem = cooldown.popleft()
                heapq.heappush(max_heap, neg_rem)

            if max_heap:
                # Phase 2A: 執行一個任務
                neg_cnt = heapq.heappop(max_heap)
                remaining = -neg_cnt - 1  # 做掉一次
                if remaining > 0:
                    ready_time = time + n + 1
                    cooldown.append((ready_time, -remaining))
                time += 1
            else:
                # Phase 2B: 無任務可執行 → idle 一拍
                time += 1

        return time
