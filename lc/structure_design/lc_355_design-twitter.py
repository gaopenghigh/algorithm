# 355. 设计推特
# 设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近 10 条推文。
# 实现 Twitter 类：
# Twitter() 初始化简易版推特对象
# void postTweet(int userId, int tweetId) 根据给定的 tweetId 和 userId 创建一条新推文。每次调用此函数都会使用一个不同的 tweetId 。
# List<Integer> getNewsFeed(int userId) 检索当前用户新闻推送中最近  10 条推文的 ID 。新闻推送中的每一项都必须是由用户关注的人或者是用户自己发布的推文。推文必须 按照时间顺序由最近到最远排序 。
# void follow(int followerId, int followeeId) ID 为 followerId 的用户开始关注 ID 为 followeeId 的用户。
# void unfollow(int followerId, int followeeId) ID 为 followerId 的用户不再关注 ID 为 followeeId 的用户。


# 抽象为合并 n 个有序链表/数组

from collections import defaultdict
from queue import PriorityQueue

class Twitter:
    def __init__(self):
        self.followed = defaultdict(lambda: set()) # userId -> set(userId,)
        self.tweets = defaultdict(lambda: []) # userId => [tweets,]
        self.revision = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.revision += 1
        # Python 的 PriorityQueue 只能从小到大，所以这里使用负的权重
        self.tweets[userId].append((-self.revision, tweetId, userId))

    def getNewsFeed(self, userId: int) -> list[int]:
        n = 10
        res = []
        users = [userId] + list(self.followed[userId])
        pq = PriorityQueue()
        for u in users:
            if self.tweets[u]:
                pq.put(self.tweets[u][-1])
        index = { u : len(self.tweets[u]) - 1 for u in users}
        while len(res) < n and not pq.empty():
            w, tId, uId = pq.get()
            res.append(tId)
            index[uId] -= 2
            if index[uId] >= 0:
                pq.put(self.tweets[uId][index[uId]])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followed[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followed[followerId]:
            self.followed[followerId].remove(followeeId)



if __name__ == '__main__':
# Your Twitter object will be instantiated and called as such:
    obj = Twitter()
    obj.postTweet(1,5)
    obj.postTweet(1,3)
    print(obj.tweets)
    print(obj.followed)
    print(obj.revision)
    print(obj.getNewsFeed(1))
    # obj.follow(1,2)
    # obj.postTweet(2,6)
    # print(obj.getNewsFeed(1))
    # obj.unfollow(1,2)
    # print(obj.getNewsFeed(1))