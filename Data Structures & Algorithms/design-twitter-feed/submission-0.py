import heapq
from collections import defaultdict
from typing import List, Tuple, Dict, Set

class Twitter:
    def __init__(self):
        self.time = 0  # 以遞減方式當時間戳，越新越小
        self.follower_map: Dict[int, Set[int]] = defaultdict(set)  # user -> followees
        self.tweet_map: Dict[int, List[Tuple[int, int]]] = defaultdict(list)  # user -> [(time, tweetId)]

    def _ensure_self_follow(self, userId: int) -> None:
        # 確保使用者能看到自己的推文
        if userId not in self.follower_map[userId]:
            self.follower_map[userId].add(userId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._ensure_self_follow(userId)
        # 新推文標記當前時間，之後 time 減 1 讓「越新越小」
        self.tweet_map[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self._ensure_self_follow(userId)

        result: List[int] = []
        min_heap: List[Tuple[int, int, int, int]] = []  # (time, tweetId, followeeId, next_index)

        # 對每個被追蹤者，推入其最新一則（列表尾端）
        for followeeId in self.follower_map[userId]:
            tweets = self.tweet_map.get(followeeId, [])
            if tweets:  # 防止空列表
                idx = len(tweets) - 1
                t, tid = tweets[idx]
                heapq.heappush(min_heap, (t, tid, followeeId, idx - 1))

        # 取最多 10 則
        while min_heap and len(result) < 10:
            t, tid, fid, idx = heapq.heappop(min_heap)
            result.append(tid)
            if idx >= 0:
                t2, tid2 = self.tweet_map[fid][idx]
                heapq.heappush(min_heap, (t2, tid2, fid, idx - 1))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self._ensure_self_follow(followerId)
        self.follower_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # 不能取消追蹤自己
        if followeeId == followerId:
            return
        if followerId in self.follower_map:
            self.follower_map[followerId].discard(followeeId)
