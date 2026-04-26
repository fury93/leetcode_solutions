class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ascii_z = (ord('z'))
        def decode(word):
            sm = sum(weights[ord(ch) - 97] for ch in word)
            return chr(ascii_z - (sm % 26))

        return ''.join(decode(w) for w in words)