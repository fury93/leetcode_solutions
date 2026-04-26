class Solution:
    def lengthOfLongestSubstringTwoDistinct2(self, s: str) -> int:
        res, pos, l = 0, defaultdict(int), 0
        for r, ch in enumerate(s):
            pos[ch] = r
            if len(pos) > 2:
                removeCh = min(pos, key=pos.get)
                l = pos[removeCh] + 1
                del pos[removeCh]
            res = max(res, r - l + 1)
        return res

    def lengthOfLongestSubstringTwoDistinct(self, s: str, k = 2) -> int:
        d, l, = defaultdict(int), 0
        for r, ch in enumerate(s):
            d[ch] += 1
            if len(d) > k:
                removeCh = s[l]
                d[removeCh] -= 1
                if d[removeCh] == 0:
                    del d[removeCh]
                l += 1
        
        return r - l + 1

class Solution2:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return n

        left, right = 0, 0
        hashmap = defaultdict()
        max_len = 2

        while right < n:
            # when the slidewindow contains less than 3 characters
            hashmap[s[right]] = right
            right += 1

            # slidewindow contains 3 characters
            if len(hashmap) == 3:
                # delete the leftmost character
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                # move left pointer of the slidewindow
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len