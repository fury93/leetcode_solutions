class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j, l1, l2 = 0, 0, len(word), len(abbr)

        while i < l1 and j < l2:
            if abbr[j].isalpha():
                if word[i] != abbr[j]: break
                i, j = i + 1, j + 1
            elif abbr[j] != '0':
                start = j
                while j < l2 and abbr[j].isdigit():
                    j += 1
                i += int(abbr[start:j])
            else:
                break

        return i == l1 and j == l2