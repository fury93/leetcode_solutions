class Solution:
    def longestBalanced(self, S: str) -> int:
        N = len(S)
        P = [[0, 0, 0]]
        for c in S:
            P.append(P[-1][:])
            P[-1]["abc".index(c)] += 1

        ans = 0
        first = {}
        for i, (a, b, c) in enumerate(P):
            for key in [
                ("abc", a - b, a - c),
                ("ab", a - b, c),
                ("bc", b - c, a),
                ("ca", c - a, b),
                ("a", b, c),
                ("b", c, a),
                ("c", a, b),
            ]:
                ans = max(ans, i - first.get(key, i))
                first.setdefault(key, i)

        return ans