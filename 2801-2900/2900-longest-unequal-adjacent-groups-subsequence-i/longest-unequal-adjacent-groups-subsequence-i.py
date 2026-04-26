class Solution2:
    # don't understand requirements
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        Result = namedtuple('Res', ['start', 'len'])
        res, l = Result(0, 1), 0

        for r in range(1, len(groups)):
            if groups[r] == groups[r-1]:
                l = r
            elif (ln:= r - l + 1) > res.len:
                res = Result(l, ln)

        return words[res.start:res.start + res.len]


class Solution:
    def getLongestSubsequence2(self, words: List[str], groups: List[int]) -> List[str]:
        ans, cur_group = [], -1
        for word, group in zip(words, groups):
            if group != cur_group:
                ans.append(word)
                cur_group = group
        return ans

    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        return [words[0]] + [words[i] for i in range(1, len(groups)) if groups[i] != groups[i - 1]]