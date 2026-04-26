class Solution:

	def maxUpgrades(self, count: list[int], upgrade: list[int], sell: list[int], money: list[int]) -> list[int]:
		res = []
		for c, u, s, m in zip(count, upgrade, sell, money):
			to_sell = ceil((c*u - m)/(s + u))
			res.append(c - to_sell if to_sell > 0 else c)
		return res