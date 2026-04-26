class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        d, maxSenderName= defaultdict(int), ''
        for mes, name in zip(messages, senders):
            d[name] += len(mes.split())
            if d[name] > d[maxSenderName]:
                maxSenderName = name
            elif d[name] == d[maxSenderName] and name > maxSenderName:
                maxSenderName = name
        
        return maxSenderName

class Solution2:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        d = defaultdict(int)
        for m, n in zip(messages, senders):
            d[n] += len(m.split())
        
        return max(d, key = lambda k: (d[k], k))