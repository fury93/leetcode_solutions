class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
            
        combined = sorted(zip(timestamp, username, website), key=lambda x: x[0])
        
        # Step 2: Map each user to their list of website visits in chronological order
        user_visits = defaultdict(list)  # Key: username, Value: list of websites
        for time, user, site in combined:
            user_visits[user].append(site)
        
        # Step 3: Generate all possible 3-sequences for each user
        # and count the number of unique users for each 3-sequence
        pattern_counts = defaultdict(int)  # Key: 3-sequence tuple, Value: count of unique users
        
        for user, sites in user_visits.items():
            if len(sites) < 3:
                continue  # Skip users with fewer than 3 website visits
            
            # Generate all possible 3-sequences using combinations with order
            # Since the sequence must respect the order of visits, we use combinations
            sequences = set(itertools.combinations(sites, 3))
            
            for seq in sequences:
                pattern_counts[seq] += 1  # Increment the count for this pattern
        
        # Step 4: Identify the 3-sequence(s) with the highest count
        # and select the lexicographically smallest one in case of ties
        max_count = 0
        result_pattern = tuple()
        
        for pattern, count in pattern_counts.items():
            if count > max_count or (count == max_count and pattern < result_pattern):
                max_count = count
                result_pattern = pattern
        
        return list(result_pattern)
        
class Solution2:
    def mostVisitedPattern(self, username, timestamp, website):
        dp = collections.defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            dp[u].append(w)
        count = sum([collections.Counter(set(itertools.combinations(dp[u], 3))) for u in dp], collections.Counter())
        return list(min(count, key=lambda k: (-count[k], k)))