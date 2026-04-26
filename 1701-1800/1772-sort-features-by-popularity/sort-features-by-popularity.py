class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:
        freq = defaultdict(int)
        for response in responses: 
            words = set(response.split())
            for feature in features: 
                if feature in words: freq[feature] += 1
        return sorted(features, key=lambda x: freq.get(x, 0), reverse=True)