class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        # Create a hash value
        def get_hash(string: str):
            key = []
            for a, b in zip(string, string[1:]):
                key.append(chr((ord(b) - ord(a)) % 26 + ord('a')))
            return ''.join(key)
        
        # Create a hash value (hash_key) for each string and append the string
        # to the list of hash values i.e. mapHashToList["cd"] = ["acf", "gil", "xzc"]
        groups = collections.defaultdict(list)
        for string in strings:
            hash_key = get_hash(string)
            groups[hash_key].append(string)
        
        # Return a list of all of the grouped strings
        return list(groups.values())

class Solution2:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def shiftChar(ch, shift):
            return (ord(ch) - shift) % 26
        
        d = defaultdict(list)
        for s in strings:
            shift = ord(s[0])
            key = tuple(shiftChar(c, shift) for c in s)
            d[key].append(s)

        return d.values()

    def groupStrings2(self, strings: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for s in strings:
            key = tuple((ord(c)-ord(s[0]))%26 for c in s)
            mp[key].append(s)
        return mp.values()
