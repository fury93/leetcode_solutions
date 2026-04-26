from sortedcontainers import SortedDict

class TimeMap:
    def __init__(self):
        self.key_time_map = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_time_map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.key_time_map: return ""
        idx = self.key_time_map[key].bisect_right(timestamp)
        
        return self.key_time_map[key].peekitem(idx-1)[1] if idx > 0 else ""