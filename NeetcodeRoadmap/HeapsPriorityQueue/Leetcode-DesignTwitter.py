from collections import defaultdict
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []
        self.follows[userId].add(userId)
        for follower in self.follows[userId]:
            if follower in self.tweets:
                index = len(self.tweets.get(follower)) - 1
                time,tweetId = self.tweets.get(follower)[index]
                heapq.heappush(heap,(time,tweetId,follower,index))

        while heap and len(res) < 10:
            time,tweetId,tweetUser,index = heapq.heappop(heap)
            res.append(tweetId)

            if index > 0:
                newTime,newTweetId = self.tweets.get(tweetUser)[index - 1]
                heapq.heappush(heap,(newTime,newTweetId,tweetUser,index - 1))
            
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)