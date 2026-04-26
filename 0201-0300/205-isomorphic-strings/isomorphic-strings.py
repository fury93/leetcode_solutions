class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(set(t))) == len(set(zip(s, t)))
    
    
    def isIsomorphic2(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        map1, map2  = {}, {}
        
        for c1, c2 in zip(s, t):
            if c1 not in map1 and c2 not in map2:
                map1[c1] = c2
                map2[c2] = c1
            elif map1.get(c1) != c2 or map2.get(c2) !=c1:
                return False
                
        return True

    #  First occurence transformation
    def transformString(self, s: str) -> str:
        index_mapping = {}
        new_str = []
        
        for i, c in enumerate(s):
            if c not in index_mapping:
                index_mapping[c] = i
            new_str.append(str(index_mapping[c]))
        
        return " ".join(new_str)
    
    def isIsomorphic3(self, s: str, t: str) -> bool:
        return self.transformString(s) == self.transformString(t)
            
            
            
        
    