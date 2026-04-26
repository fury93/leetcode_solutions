class Solution:
    def mostBooked2(self, n: int, meetings: List[List[int]]) -> int:
        res = [0] * n
        rooms = [(0,i) for i in range(n)] # (availabilityTime, roomId)
        meetings.sort()
        for start, end in meetings:
            while rooms and rooms[0][0] < start:
                _, room = heappop(rooms)
                heappush(rooms, (start, room))
            release, room = heappop(rooms)
            heappush(rooms, (release + (end-start), room))
            res[room] += 1
        
        return res.index(max(res))
    
    def mostBooked3(self, n: int, meetings: List[List[int]]) -> int:
        booked, free, freq = [], list(range(n)), defaultdict(int)
        meetings.sort()

        for start, end in meetings:
            while booked and booked[0][0] <= start:
                _, room = heappop(booked)
                heappush(free, room)
            
            if free:
                room = heapq.heappop(free)
                heappush(booked, (end, room))
            else:
                release, room = heappop(booked)
                heappush(booked, (release + (end - start), room))
            
            freq[room] += 1

        return max(freq, key=freq.get)

    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        booked, free, res = [], list(range(n)), [0] * n
        for start, end in sorted(meetings):
            while booked and booked[0][0] <= start:
                _, room = heappop(booked)
                heappush(free, room)
            if free:
                room = heappop(free)
                heappush(booked, (end, room))
            else:
                release, room = heappop(booked)
                heappush(booked, (release + (end - start), room))
            res[room] += 1
        return res.index(max(res))