class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friendsSet = set(friends)
        return [i for i in order if i in friendsSet]

    def recoverOrder2(self, order: List[int], friends: List[int]) -> List[int]:
        pos = {v: i for i, v in enumerate(order)}
        return list(sorted(friends, key = pos.get))