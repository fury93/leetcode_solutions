from sortedcontainers import SortedSet

class FileSharing:

    def __init__(self, m: int):
        self.users = {}
        self.chunks = {}
        self.cur_id = 1
        self.used_ids = []
        heapify(self.used_ids)
        
    def join(self, ownedChunks: List[int]) -> int:
        if len(self.used_ids) != 0:
            user_id = heappop(self.used_ids)
        else:
            user_id = self.cur_id
            self.cur_id += 1
        self.users[user_id] = ownedChunks
        for chuck in ownedChunks:
            if not chuck in self.chunks:
                self.chunks[chuck] = SortedSet()
            self.chunks[chuck].add(user_id)
        return user_id
        
    def leave(self, userID: int) -> None:
        for chunk in self.users[userID]:
            if chunk in self.chunks and userID in self.chunks[chunk]:
                self.chunks[chunk].remove(userID)
        del self.users[userID]
        heappush(self.used_ids, userID)

    def request(self, userID: int, chunkID: int) -> List[int]:
        res = []
        if chunkID in self.chunks and len(self.chunks[chunkID]) > 0:
            res = list(self.chunks[chunkID])
            self.chunks[chunkID].add(userID)
            self.users[userID].append(chunkID)
        return res

class FileSharing2:

    def __init__(self, m: int):
        self.user_to_chunks = {}
        self.available_ids = []
        heapq.heappush(self.available_ids, 1) 

    def join(self, ownedChunks: List[int]) -> int:
        id = heapq.heappop(self.available_ids)
        if len(self.available_ids) == 0:
            heapq.heappush(self.available_ids, id + 1) 
        self.user_to_chunks[id] = set(ownedChunks)
        return id

    def leave(self, userID: int) -> None:
        heapq.heappush(self.available_ids, userID)
        del self.user_to_chunks[userID]

    def request(self, userID: int, chunkID: int) -> List[int]:
        chunk_owners = []
        for ownerID, chunkIDs in self.user_to_chunks.items():
            if chunkID in chunkIDs:
                chunk_owners.append(ownerID)
        if len(chunk_owners) > 0:
            self.user_to_chunks[userID].add(chunkID)
        return sorted(chunk_owners)

# Your FileSharing object will be instantiated and called as such:
# obj = FileSharing(m)
# param_1 = obj.join(ownedChunks)
# obj.leave(userID)
# param_3 = obj.request(userID,chunkID)