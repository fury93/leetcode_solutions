class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        allDamage, maxLevelDamage = 0, 0
        for levelDamage in damage:
            allDamage += levelDamage
            maxLevelDamage = max(maxLevelDamage, levelDamage)
        
        return allDamage - min(armor, maxLevelDamage) + 1

class Solution2:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        tot = sum(damage)
        tot -= min(armor, max(damage))
        return tot + 1