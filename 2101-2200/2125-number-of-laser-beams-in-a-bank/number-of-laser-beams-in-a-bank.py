class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev, res = 0, 0
        for row in bank:
            devices = row.count('1')
            if not devices: continue
            res += prev * devices
            prev = devices
        return res