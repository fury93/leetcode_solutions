class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbr = dict()
        for w in dictionary:
            key = self.convertToAbbr(w)
            if key in self.abbr and self.abbr[key] != w:
                self.abbr[key] = ''
            else:
                self.abbr[key] = w

    def isUnique(self, word: str) -> bool:
        key = self.convertToAbbr(word)
        return not key in self.abbr or self.abbr[key] == word

    def convertToAbbr(self, w):
        return w if (ln:=len(w)) < 2 else f'{w[0]}{ln-2}{w[-1]}'

class ValidWordAbbr2:

    def __init__(self, dictionary: List[str]):
        self.abbr = defaultdict(set)
        for w in dictionary:
            self.abbr[self.convertToAbbr(w)].add(w)

    def isUnique(self, word: str) -> bool:
        key = self.convertToAbbr(word)
        return not self.abbr[key] or len(self.abbr[key]) == 1 and word in self.abbr[key]

    def convertToAbbr(self, w):
        return f'{w[0]}{ln-2 if (ln:=len(w)) > 2 else ""}{w[-1]}'