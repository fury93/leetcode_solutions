class Excel:

    def __init__(self, H: int, W: str):
        self.height, self.width = H, self._map(W) + 1
        self.form = [[0]*self.width for _ in range(self.height)]
    
    def _map(self, char):
        return ord(char) - 65

    def set(self, r: int, c: str, v: int) -> None:
        self.form[r-1][self._map(c)] = v

    def get(self, r: int, c: str) -> int:
        r, c = r-1, self._map(c)
        if type(self.form[r][c]) is int:
            return self.form[r][c]
        return sum(self.get(i+1, chr(j+65)) * self.form[r][c][(i, j)] for i, j in self.form[r][c])
    
    def _parse(self, string: str):
        i = int(''.join(char for char in string if char.isdigit())) - 1
        j = self._map([char for char in string if char.isalpha()][0])
        return i, j
        
    def sum(self, r: int, c: str, strs: List[str]) -> int:
        cells = collections.defaultdict(int)
        for string in strs:
            if ':' not in string:
                i, j = self._parse(string)
                cells[(i, j)] += 1
            else:
                start, end = string.split(':')
                i0, j0 = self._parse(start)
                i1, j1 = self._parse(end)
                for i in range(i0, i1+1):
                    for j in range(j0, j1+1):
                        cells[(i, j)] += 1
        self.form[r-1][self._map(c)] = cells
        return self.get(r, c)

# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)