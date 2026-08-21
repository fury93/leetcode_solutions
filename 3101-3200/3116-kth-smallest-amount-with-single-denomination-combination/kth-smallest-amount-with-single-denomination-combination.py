class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        filtered_coins: List[int] = []
        for index in range(len(coins)):
            is_valid = True
            for previous_index in range(index):
                if coins[index] % coins[previous_index] == 0:
                    is_valid = False
                    break
            if is_valid:
                filtered_coins.append(coins[index])
        smallest_possible = filtered_coins[0]
        largest_possible = filtered_coins[0] * k
        lcms_to_add: List[int] = []
        lcms_to_substract: List[int] = []
        for r in range(2, 16):
            if r % 2 == 0:
                for combo in combinations(filtered_coins, r):
                    lcms_to_substract.append(lcm(*combo))
            else:
                for combo in combinations(filtered_coins, r):
                    lcms_to_add.append(lcm(*combo))

        def is_possible(num: int) -> bool:
            count_nums = 0
            for coin in filtered_coins:
                count_nums += num // coin
            for lcm_to_add in lcms_to_add:
                count_nums += num // lcm_to_add
            for lcm_to_subtract in lcms_to_substract:
                count_nums -= num // lcm_to_subtract
            return count_nums >= k

        while largest_possible > smallest_possible:
            mid = (smallest_possible + largest_possible) // 2
            if is_possible(mid):
                largest_possible = mid
            else:
                smallest_possible = mid + 1
        return smallest_possible


    def findKthSmallest2(self, coins: List[int], k: int) -> int:
        coins.sort()
        n = len(coins)
        m = 1 << n
        left = k
        right = coins[0] * k + 1

        bit_count = [0] * m
        lcm = [0] * m

        for mask in range(1, m):
            cur_lcm = 1

            for i, coin in enumerate(coins):
                if mask >> i & 1:
                    cur_lcm = cur_lcm // gcd(cur_lcm, coin) * coin
                    bit_count[mask] += 1

            lcm[mask] = cur_lcm

        def count(x: int) -> int:
            res = 0

            for mask in range(1, m):
                if lcm[mask] <= x:
                    if bit_count[mask] & 1:
                        res += x // lcm[mask]
                    else:
                        res -= x // lcm[mask]

            return res

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left