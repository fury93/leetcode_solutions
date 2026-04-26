class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        def ip_to_num(ip):
            components = map(int, ip.split('.'))
            return (next(components) << 24) + (next(components) << 16) + (next(components) << 8) + next(components)
        def num_to_ip(num):
            mask = (1 << 8) - 1
            return f'{num>>24}.{(num>>16) & mask}.{(num>>8) & mask}.{num & mask}'
        res = []
        from math import log2
        num = ip_to_num(ip)
        while n > 0:
            if num == 0:
                low_bit = 1 << 32
            else:
                low_bit = num & (-num)
            while low_bit > n:
                low_bit >>= 1
            n -= low_bit
            res.append(f'{num_to_ip(num)}/{32 - int(log2(low_bit))}')
            num += low_bit
        return res