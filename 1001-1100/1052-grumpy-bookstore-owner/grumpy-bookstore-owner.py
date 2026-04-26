class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied, notSatisfiedGroup, maxNotSatisfiedGroup, k = 0, 0, 0, minutes
        for i, (cnt, g) in enumerate(zip(customers, grumpy)):
            if not g:
                satisfied += cnt
            else:
                notSatisfiedGroup += cnt

            if i >= k and grumpy[i-k]:
                notSatisfiedGroup -= customers[i-k]
            maxNotSatisfiedGroup = max(maxNotSatisfiedGroup, notSatisfiedGroup)

        return satisfied + maxNotSatisfiedGroup
