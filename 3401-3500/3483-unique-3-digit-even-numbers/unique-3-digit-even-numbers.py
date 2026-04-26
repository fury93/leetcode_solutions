class Solution:
    # O(N + U^3), where U is uniq digits <= 900 (constant)
    def totalNumbers(self, digits: list[int]) -> int:
        cnt = Counter(digits)
        uniq = cnt.keys()
        res = 0

        for i in uniq:
            if i == 0: continue
            cnt[i] -= 1
            
            for j in uniq:
                if cnt[j] == 0: continue
                cnt[j] -= 1
                
                for k in uniq:
                    if cnt[k] > 0 and not k & 1:
                        res += 1
                
                cnt[j] += 1
            
            cnt[i] += 1

        return res


    # O(N^3)
    def totalNumbers1(self, digits: list[int]) -> int:
        numbers = set()

        for a, b, c in permutations(digits, 3):
            if c % 2 == 0 and a != 0:
                numbers.add((a, b, c))

        return len(numbers)

    # O(N + 450 * (3 + 10)) => O(N)
    def totalNumbers2(self, digits: List[int]) -> int:
        cnt = Counter(map(str, digits))
        return sum(cnt >= Counter(str(n)) for n in range(100, 1000, 2))