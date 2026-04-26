class Solution:
    # bijection
    def wordPattern3(self, pattern: str, s: str) -> bool:
        s = s.split()
        return (len(set(pattern)) ==
                len(set(s)) ==
                len(set(zip_longest(pattern,s))))

    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        charToWord, wordToChar = {}, {}
        for char, word in zip(pattern, words):
            if char in charToWord and charToWord[char] != word:
                return False
            if word in wordToChar and wordToChar[word] != char:
                return False
            charToWord[char] = word
            wordToChar[word] = char
            continue
            # old approach
            if c not in dic1 and word not in dic2:
                dic1[c] = word
                dic2[word] = c
            elif dic1.get(c) != word or dic2.get(word) != c:
                return False
        return True
            