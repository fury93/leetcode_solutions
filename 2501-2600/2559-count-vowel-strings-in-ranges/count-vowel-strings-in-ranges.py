class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiuo')
        prefix = [0] * (len(words) + 1)

        for i, w in enumerate(words, start = 1):
            if w[0] in vowels and w[-1] in vowels:
                prefix[i] = prefix[i-1] + 1
            else:
                prefix[i] = prefix[i-1]

        return [prefix[end+1] - prefix[start] for start, end in queries]