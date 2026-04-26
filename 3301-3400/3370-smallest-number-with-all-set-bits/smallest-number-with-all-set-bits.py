class Solution:
    def smallestNumber(self, n: int) -> int:
        n_bin = bin(n)
        firstOnePos = n_bin.find('1')
        if firstOnePos == -1:
            return 1
        
        x_bin = '1' * (len(n_bin) - firstOnePos)
        
        return int(x_bin, 2)