class ThroneInheritance:

    def __init__(self, kingName: str):
        self.familyTree = collections.defaultdict(list)
        self.dead = set()
        self.king = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.familyTree[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        
        def dfs(name: str) -> None:
            if name not in self.dead:
                inheritance_order.append(name)
            for kid in self.familyTree[name]:
                dfs(kid)

        inheritance_order = []
        dfs(self.king)
        return inheritance_order
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()