class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tables = defaultdict(lambda: defaultdict(int))
        foods = set()
        for _, table, food in orders:
            foods.add(food)
            tables[table][food] += 1

        sortedFoods = sorted(foods)
        foodId = {f:i for i, f in enumerate(sortedFoods)}

        res = [["Table"] + sortedFoods]
        for table in sorted(tables.keys(), key = int):
            row = ["0"] * (len(sortedFoods))
            for food in tables[table]:
                row[foodId[food]] = str(tables[table][food])
            res.append([table] + row)

        return res