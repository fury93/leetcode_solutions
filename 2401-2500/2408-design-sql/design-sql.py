class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.d = defaultdict(list)

    def insertRow(self, name: str, row: List[str]) -> None:
        self.d[name].append(row)
        
    def deleteRow(self, name: str, rowId: int) -> None:
        pass

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.d[name][rowId-1][columnId-1]

class SQL2:

    def __init__(self, names: List[str], columns: List[int]):
        self.tables = {name: {} for name in names}

    def insertRow(self, name: str, row: List[str]) -> None:
        idx = len(self.tables[name]) + 1
        self.tables[name][idx] = row

    def deleteRow(self, name: str, rowId: int) -> None:
        return

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.tables[name][rowId][columnId-1]
        


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)