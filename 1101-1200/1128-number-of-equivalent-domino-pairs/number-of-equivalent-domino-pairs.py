class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt = Counter(tuple(sorted(d)) for d in dominoes)
        return sum((x * (x-1))//2 for x in cnt.values())