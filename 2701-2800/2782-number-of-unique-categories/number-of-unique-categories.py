# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass
class Solution:
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
        res = n
        for i in range(n):
            for j in range(i):
                if categoryHandler.haveSameCategory(i, j):
                    res -= 1
                    break

        return res

