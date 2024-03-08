class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count=0
        max_freq=0
        H=defaultdict(int)
        for num in nums:
            H[num]+=1
            if H[num]>max_freq:
                count=1
                max_freq=H[num]
            elif H[num]==max_freq:
                count+=1
        return count*max_freq            