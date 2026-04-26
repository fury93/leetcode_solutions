class Solution:
    def killProcess(self, pid, ppid, kill):
        d = collections.defaultdict(list)
        for c, p in zip(pid, ppid): d[p].append(c)
        bfs = [kill]
        for i in bfs: bfs.extend(d.get(i, []))
        return bfs