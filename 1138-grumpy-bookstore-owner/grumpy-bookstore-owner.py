class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n=len(customers)
        satisfied=sum(customers[:minutes])

        satisfied+=sum( (1-grumpy[i])*customers[i] for i in range(minutes, n))

        max_satisfied=satisfied

        for i in range(minutes, n):
            satisfied-=grumpy[i-minutes]*customers[i-minutes]
            satisfied+=grumpy[i]*customers[i]
            max_satisfied = max(max_satisfied, satisfied)

        return max_satisfied
        