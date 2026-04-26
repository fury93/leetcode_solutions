class VideoSharingPlatform:

    def __init__(self):
        self.h=[]
        self.mx=0
        self.vid={}

    def upload(self, video: str) -> int:
        if self.h:
            videoId=heapq.heappop(self.h)
        else:
            videoId=self.mx
            self.mx+=1
        self.vid[videoId]=[video,0,0,0]     #[string,likes,dislikes,views]
        return videoId

    def remove(self, videoId: int) -> None:
        if videoId not in self.vid: return
        heapq.heappush(self.h,videoId)
        del self.vid[videoId]

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if videoId in self.vid:
            self.vid[videoId][3]+=1
            s=self.vid[videoId][0]
            return s[startMinute:min(endMinute+1,len(s))]
        return '-1'

    def like(self, videoId: int) -> None:
        if videoId in self.vid: self.vid[videoId][1]+=1

    def dislike(self, videoId: int) -> None:
        if videoId in self.vid: self.vid[videoId][2]+=1

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        return self.vid[videoId][1:3] if videoId in self.vid else [-1]

    def getViews(self, videoId: int) -> int:
        return self.vid[videoId][3] if videoId in self.vid else -1