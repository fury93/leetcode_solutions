class Fenwick:
    def __init__(self, n: int) -> None:
        self.n = n
        self.bit1 = [0] * (n + 1)
        self.bit2 = [0] * (n + 1)

    def _add(self, bit: list[int], idx: int, delta: int) -> None:
        while idx <= self.n:
            bit[idx] += delta
            idx += idx & -idx

    def range_add(self, left: int, right: int, delta: int) -> None:
        if left > right:
            return
        n = self.n
        self._add(self.bit1, left, delta)
        if right + 1 <= n:
            self._add(self.bit1, right + 1, -delta)

        self._add(self.bit2, left, delta * (left - 1))
        if right + 1 <= n:
            self._add(self.bit2, right + 1, -delta * right)

    def _prefix_sum(self, bit: list[int], idx: int) -> int:
        total = 0
        while idx > 0:
            total += bit[idx]
            idx -= idx & -idx
        return total

    def prefix_sum(self, idx: int) -> int:
        if idx <= 0:
            return 0
        return self._prefix_sum(self.bit1, idx) * idx - self._prefix_sum(self.bit2, idx)

    def range_sum(self, left: int, right: int) -> int:
        if left > right:
            return 0
        return self.prefix_sum(right) - self.prefix_sum(left - 1)


class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        mod = 1_000_000_007
        n = len(nums)
        bit = Fenwick(n)
        last: dict[int, int] = {}
        total_sq = 0
        ans = 0

        for right, value in enumerate(nums):
            left = last.get(value, -1) + 1
            curr_sum = bit.range_sum(left + 1, right + 1)
            length = right - left + 1
            total_sq = (total_sq + 2 * curr_sum + length) % mod
            bit.range_add(left + 1, right + 1, 1)
            ans = (ans + total_sq) % mod
            last[value] = right

        return ans
        
class BIT:
    def __init__(self, n: int):
        self.size = n
        self._tree1 = defaultdict(int)
        self._tree2 = defaultdict(int)

    def _lowbit(self, index: int) -> int:
        return index & -index

    def add(self, left: int, right: int, delta: int) -> None:
        self._add(left, delta)
        self._add(right + 1, -delta)

    def query(self, left: int, right: int) -> int:
        return self._query(right) - self._query(left - 1)

    def _add(self, index: int, delta: int) -> None:
        index += 1
        rawIndex = index
        while index <= self.size:
            self._tree1[index] += delta
            self._tree2[index] += (rawIndex - 1) * delta
            index += self._lowbit(index)

    def _query(self, index: int) -> int:
        index += 1
        if index > self.size:
            index = self.size

        rawIndex = index
        res = 0
        while index > 0:
            res += rawIndex * self._tree1[index] - self._tree2[index]
            index -= self._lowbit(index)
        return res


class Solution2:
    def sumCounts(self, A: List[int]) -> int:
        n = len(A)
        res = cur = 0
        bit = BIT(n + 10)
        seen = {}
        mod = 10**9 + 7
        for i, a in enumerate(A):
            j = seen.get(a, -1) + 1
            cur = (cur + bit.query(j, i) * 2 + i - j + 1) % mod
            res = (res + cur) % mod
            bit.add(j, i, 1)
            seen[a] = i
        return res