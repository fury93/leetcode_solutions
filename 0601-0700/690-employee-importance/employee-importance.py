"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    # BFS
    def getImportance2(self, employees: List['Employee'], id: int) -> int:
        employeeById = {e.id: e for e in employees}
        totalImportance, q = 0, deque([id])
        
        while q:
            employee = employeeById[q.popleft()]
            totalImportance += employee.importance
            q.extend(employee.subordinates)

        return totalImportance

    # DFS
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employeeById = {e.id: e for e in employees}

        def dfs(idx):
            e = employeeById[idx]
            return e.importance + sum(dfs(idx) for idx in e.subordinates)
        
        return dfs(id)
            