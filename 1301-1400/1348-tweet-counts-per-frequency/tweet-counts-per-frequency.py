class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if tweetName not in self.tweets: return 0

        match freq:
            case 'minute': intervalSize = 60
            case 'hour': intervalSize = 3600
            case _: intervalSize = 86400

        intervalCnt = (endTime - startTime) // intervalSize + 1
        results = [0] * intervalCnt
        
        for time in self.tweets[tweetName]:
            if startTime <= time <= endTime:
                results[(time-startTime) // intervalSize] += 1
        
        return results


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)