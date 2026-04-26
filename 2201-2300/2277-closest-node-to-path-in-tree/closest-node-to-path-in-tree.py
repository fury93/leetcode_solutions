class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        G = defaultdict(list)
        for a,b in edges:
            G[a].append(b)
            G[b].append(a)
        depths = [0]*n
        binaryParents = [[0]*16 for _ in range(n)]
        def dfs(node, parents,depth):
            depths[node]=depth
            for bit in range(16):
                if 1<<bit <= len(parents):
                    binaryParents[node][bit] = parents[-(1<<bit)]
            parents.append(node)
            for nxt in G[node]:
                if len(parents)>=2 and nxt==parents[-2]:
                    continue
                dfs(nxt,parents,depth+1)
            parents.pop()
        dfs(0,[],0)
        def getKthParent(node,k):
            if not k: 
                return node
            bit=0
            while (1<<(bit+1)) <= k: 
                bit+=1
            return getKthParent(binaryParents[node][bit],k&(~(1<<bit)))
        def lca(a,b):
            if depths[a]>depths[b]:
                return lca(b,a)
            b = getKthParent(b,depths[b]-depths[a])
            if a==b:
                return a
            for i in range(len(binaryParents[a])-1,-1,-1):
                if binaryParents[a][i]!=binaryParents[b][i]:
                    a,b = binaryParents[a][i],binaryParents[b][i]
            return binaryParents[a][0]
        return [max([lca(a,b),lca(a,q),lca(b,q)],key=lambda x:depths[x]) for a,b,q in query]