class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        index = collections.defaultdict(set)
        dictionary = set(word for word in dictionary if len(word) == len(target))
        
        # check the trivial case
        if len(target) not in map(len, dictionary):
            return str(len(target))
        
        # build the index
        for word in dictionary:
            for i, c in enumerate(word):
                index[i, c].add(word)
        
        def replace(word: str, i: int, target: str) -> str:
            return word[:i] + target[i] + word[i+1 :]
    
        def abbrev(word: str) -> str:
            return re.sub(r'\?+', lambda m: str(len(m.group())), word)
        
        def abbrev_cost(word: str) -> str:
            return len(re.sub(r'\?+', '?', word))
        
        # A* search
        queue = []                  # min heap, elements are tuples (cost, wildcard)
        word = '?' * len(target)    # wildcards are like app?e, we start with all ????? and replace them one by one
        
        for i, c in enumerate(word):
            mod_word = replace(word, i, target)
            heapq.heappush(queue, (abbrev_cost(mod_word), mod_word))
        
        while queue:
            _, word = heapq.heappop(queue)

            # count conflicts
            all_words = copy.copy(dictionary)

            for j, c in enumerate(word):
                if c != '?':
                    all_words &= index[j, c]

            num_conflicts = len(all_words)
            
            if num_conflicts == 0:
                return abbrev(word)

            for i, c in enumerate(word):
                if c == '?':
                    mod_word = replace(word, i, target)
                    heapq.heappush(queue, (abbrev_cost(mod_word) + num_conflicts, mod_word))

class Solution2:
    def minAbbreviation(self, target, dictionary):
        m = len(target)
        diffs = {sum(2**i for i, c in enumerate(word) if target[i] != c)
                for word in dictionary if len(word) == m}
        if not diffs:
            return str(m)
        bits = max((i for i in range(2**m) if all(d & i for d in diffs)),
                key=lambda bits: sum((bits >> i) & 3 == 0 for i in range(m-1)))
        s = ''.join(target[i] if bits & 2**i else '#' for i in range(m))
        return re.sub('#+', lambda m: str(len(m.group())), s)