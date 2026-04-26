from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = {}
        self.data = defaultdict(SortedSet)
        for food, cuisine, rating in zip(foods, cuisines, ratings): 
            self.foods[food] = (cuisine, rating)
            self.data[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.foods[food]
        self.foods[food] = cuisine, newRating
        self.data[cuisine].remove((-rating, food))
        self.data[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.data[cuisine][0][1]

class FoodRatings2:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines = {}
        self.ratings = {}
        self.cuisinessFoods = defaultdict(SortedSet)

        for i, food in enumerate(foods):
            self.cuisines[food] = cuisines[i]
            self.ratings[food] = ratings[i]
            self.cuisinessFoods[cuisines[i]].add((-ratings[i], food))

    def changeRating(self, food: str, newRating: int) -> None:
        oldRating = self.ratings[food]
        cuisines = self.cuisines[food]
        # remove
        self.cuisinessFoods[cuisines].remove((-oldRating, food))
        # update
        self.ratings[food] = newRating
        self.cuisinessFoods[cuisines].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.cuisinessFoods[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)