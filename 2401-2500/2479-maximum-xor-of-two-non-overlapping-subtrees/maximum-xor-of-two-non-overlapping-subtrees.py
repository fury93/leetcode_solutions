class Solution:
    def maxXor(self, n: int, edges: List[List[int]], values: List[int]) -> int:
        
        def countSubTreeValues(root, parent):

            for child in adj[root]:
                if child != parent:
                    values[root] += countSubTreeValues(child, root)

            return values[root]

        def findMaxXor(root, parent):

            #Generate binary number of the subtree value
            num = bin(values[root])[2:]
            arr = [0] * (50-len(num)) + list(map(int, num))

            #Find the max xor for current subtree value
            if self.trie:
                trie = self.trie
                temp = []
                for item in arr:
                    if item ^ 1 in trie:
                        temp.append('1')
                        trie = trie[item ^ 1]
                    else:
                        temp.append('0')
                        trie = trie[item]
                self.maxi = max(self.maxi, int(''.join(temp), 2))
            
            #DFS
            for child in adj[root]:
                if child != parent:
                    findMaxXor(child, root)
            
            #Add subtree value to trie
            trie = self.trie
            for item in arr:
                if not item in trie:
                    trie[item] = {}
                trie = trie[item]

        #Build adj
        adj = defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        self.trie = {}
        self.maxi = 0
        countSubTreeValues(0, 0)
        findMaxXor(0, 0)

        return self.maxi