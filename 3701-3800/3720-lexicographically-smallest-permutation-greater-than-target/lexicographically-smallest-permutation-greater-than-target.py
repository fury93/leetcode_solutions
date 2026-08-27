class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        # Consume as much of target's prefix as the multiset allows.
        p = 0
        while p < n:
            c = ord(target[p]) - 97
            if cnt[c] == 0:
                break
            cnt[c] -= 1
            p += 1

        i = p
        while i >= 0:
            if i < n:
                t = ord(target[i]) - 97
                pick = -1
                for c in range(t + 1, 26):
                    if cnt[c] > 0:
                        pick = c
                        break
                if pick >= 0:
                    cnt[pick] -= 1
                    tail = ''.join(chr(97 + c) * cnt[c] for c in range(26))
                    cnt[pick] += 1
                    return target[:i] + chr(97 + pick) + tail
            i -= 1
            if i >= 0:
                cnt[ord(target[i]) - 97] += 1
        return ""
        
    def lexGreaterPermutation2(self, s: str, target: str) -> str:
        cnt = [0] * 26
        for i in range(len(s)):
            cnt[ord(s[i]) - ord("a")] += 1
            cnt[ord(target[i]) - ord("a")] -= 1

        # Try from right to left
        t = list(target)
        for i in range(len(s) - 1, -1, -1):
            b = ord(t[i]) - ord("a")
            cnt[b] += 1  # Reversal of consumption
            # Check if the prefix can fully match
            if min(cnt) < 0:
                continue
            # Find the smallest available character larger than b.
            for j in range(b + 1, 26):
                if cnt[j] > 0:
                    cnt[j] -= 1
                    t[i] = chr(ord("a") + j)
                    return "".join(t[: i + 1]) + self.getMinString(cnt)

        return ""

    # Get the lexicographically smallest string (in ascending order)
    def getMinString(self, cnt: list[int]) -> str:
        res = []
        for i in range(26):
            res.append(chr(ord("a") + i) * cnt[i])
        return "".join(res)