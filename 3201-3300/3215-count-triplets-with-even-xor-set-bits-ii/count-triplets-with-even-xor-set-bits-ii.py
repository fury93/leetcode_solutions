class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        c_a = Counter([(x.bit_count() % 2) for x in a])
        c_b = Counter([(x.bit_count() % 2) for x in b])
        c_c = Counter([(x.bit_count() % 2) for x in c])

        ans = 0
        ans += (c_a[0] * c_b[0] * c_c[0])
        ans += (c_a[1] * c_b[1] * c_c[0])
        ans += (c_a[1] * c_b[0] * c_c[1])
        ans += (c_a[0] * c_b[1] * c_c[1])

        return ans