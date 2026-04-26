class Solution:
    def maxDepthBST(self, order: List[int]) -> int:
        n = len(order)
        parents = [0]*(n+1)
        insert_orders = [0]*(n+1)
        for i,v in enumerate(order,1):
            insert_orders[v]=i
        stack = [] # increasing insert order
        for node,insert_order in enumerate(insert_orders):
            while stack and insert_orders[stack[-1]]>insert_order:
                prevNode = stack.pop()
                if insert_orders[parents[prevNode]]<insert_order:
                    parents[prevNode] = node
            if stack:
                parents[node]=stack[-1]
            stack.append(node)
        depths = [0]*(n+1)
        for num in order:
            depths[num]=depths[parents[num]]+1
        return max(depths)