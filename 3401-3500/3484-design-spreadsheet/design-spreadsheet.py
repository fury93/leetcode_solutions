class Spreadsheet:

    def __init__(self, rows: int):
        self.spreadsheet = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.spreadsheet[cell] = value

    def resetCell(self, cell: str) -> None:
        self.spreadsheet[cell] = 0

    def getValue(self, formula: str) -> int:
        return sum(map(self._mapToValue, formula[1 :].split('+')))

    def _mapToValue(self, s: str) -> int:
        return int(s) if s.isdigit() else self.spreadsheet[s]

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)