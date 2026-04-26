class Solution:
    def countDistinctStrings(self, s: str, k: int) -> int:
	    # Python handles arbitrarily large integers, thus,
		# it's safe to use just this one-liner (no overflows)
        return (1 << (len(s)-k+1)) % 1_000_000_007