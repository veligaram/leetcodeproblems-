class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        result = [1] * nums_length
        pre = 1
        for i in range(nums_length):
            result[i] = result[i] * pre
            pre = pre * nums[i]
        
        suf = 1
        for i in range(nums_length - 1, -1, -1):
            result[i] = result[i] * suf
            suf = suf * nums[i]

        return result