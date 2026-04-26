class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        pos = {n:i for i, n in enumerate(arr2)}
        return sorted(arr1, key = lambda x: pos[x] if x in pos else 1000 + x)


    def relativeSortArray2(self, arr1: List[int], arr2: List[int]) -> List[int]:
        part1, part2, d, arr2_set = [], [], defaultdict(int), set(arr2)
        
        for n in arr1:
            if n in arr2_set: d[n] += 1
            else: part2.append(n)

        for n in arr2:
            part1.extend([n] * d[n])
        
        return part1 + sorted(part2)