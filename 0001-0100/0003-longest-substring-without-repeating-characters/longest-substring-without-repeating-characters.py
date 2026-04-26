class Solution:
    # Optimized Sliding Window with list
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, pos, l = 0, [-1] * 128, 0
        for r, ch in enumerate(s):
            idx = ord(ch)
            if pos[idx] >= l:
                l = pos[idx] + 1
            res = max(res, r - l + 1)
            pos[idx] = r
        return res

    # Optimized Sliding Window with HashMap
    def lengthOfLongestSubstring2(self, s: str) -> int:
        res, pos, l = 0, defaultdict(int), 0
        for r, ch in enumerate(s):
            if ch in pos:
                l = max(l, pos[ch] + 1)
            res = max(res, r - l + 1)
            pos[ch] = r
        return res

    # Not optimized Sliding Window
    def lengthOfLongestSubstring3(self, s: str) -> int:
        chars = Counter()

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[r] += 1

            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res

    # Brute-force
    def lengthOfLongestSubstring4(self, s: str) -> int:
        def check(start, end):
            chars = set()
            for i in range(start, end + 1):
                c = s[i]
                if c in chars:
                    return False
                chars.add(c)
            return True

        n = len(s)

        res = 0
        for i in range(n):
            for j in range(i, n):
                if check(i, j):
                    res = max(res, j - i + 1)
        return res