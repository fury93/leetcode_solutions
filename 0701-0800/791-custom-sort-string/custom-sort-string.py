#from itertools import repeat
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = defaultdict(int)
        for ch in s:
            freq[ch] += 1
        
        chars = []
        for ch in order:
            if freq[ch] > 0:
                chars.append(repeat(ch, freq[ch]))
                freq[ch] = 0

        for ch, cnt in freq.items():
            if cnt > 0:
                chars.append(repeat(ch, cnt))

        return ''.join(chain.from_iterable(chars))

    def customSortString2(self, order: str, s: str) -> str:
        d = {v:k for k, v in enumerate(order)}
        return ''.join(sorted(s, key=lambda ch: d[ch] if ch in d else len(s)))

    def customSortString3(self, order: str, s: str) -> str:
        cnt = Counter(s)
        chars1 = [repeat(ch, cnt[ch]) for ch in order]
        chars2 = [repeat(ch, cnt) for ch, cnt in cnt.items() if ch not in order]
        return ''.join(chain(*chars1, *chars2))