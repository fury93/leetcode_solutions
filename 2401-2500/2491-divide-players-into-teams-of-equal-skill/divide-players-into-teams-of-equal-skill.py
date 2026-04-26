class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        d, S, groups = defaultdict(int), 0, len(skill) // 2
        #caclulate skills sum and frequency
        for n in skill:
            d[n] += 1
            S += n
        
        if S % groups: return -1
        groupSkill = S // groups

        chemistry, seen = 0, set()
        for personSkill, personCount in d.items():
            if personSkill in seen: continue
            
            partnerSkill = groupSkill - personSkill
            seen.update([personSkill, partnerSkill])
            #group with people with the same skill only
            if personSkill == partnerSkill:
                if personCount & 1: return -1
                chemistry += personCount//2 * personSkill**2
                continue
            
            if personCount != d[partnerSkill]: return -1
            chemistry += (personSkill * partnerSkill) * personCount

        return chemistry