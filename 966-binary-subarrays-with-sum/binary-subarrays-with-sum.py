class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ones = [-1]
        for i, x in enumerate(nums):
            if x:
                ones.append(i)
        ones.append(len(nums))
        l, r = 0, goal + 1
        tot = 0
        while r < len(ones):
            if goal:
                tot += (ones[l+1] - ones[l]) * (ones[r] - ones[r-1])
            else:
                zeroes = ones[r] - ones[l]
                tot += zeroes * (zeroes - 1) // 2
            l += 1
            r += 1
        return tot