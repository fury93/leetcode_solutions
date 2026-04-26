class Solution:
    def minimumKeypresses(self, s: str) -> int:
        freq = sorted(Counter(s).values(), reverse=True)
        return sum((i // 9 + 1) * f for i, f in enumerate(freq))

class Solution2:
    def minimumKeypresses(self, s: str) -> int:
        c = collections.Counter(s)
        ans = cnt = 0
        for i, freq in enumerate(sorted(c.values(), reverse=True)):  # sort reversely
            if i % 9 == 0:
                cnt += 1
            ans += cnt * freq                                        # add `num_of_time_to_press_the_key * frequency` to result
        return ans
