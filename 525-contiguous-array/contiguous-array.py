class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = {0: -1}
        max_len = count_diff = 0
        
        for i, num in enumerate(nums):
            count_diff += 1 if num == 1 else -1
            if count_diff in count:
                max_len = max(max_len, i - count[count_diff])
            else:
                count[count_diff] = i
        
        return max_len