class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        

        def dfs(subset, curr, nums, start):
            subset.add(tuple(curr))
            for i in range(start,len(nums)):
                curr.append(nums[i]) 
                dfs(subset,curr,nums,i+1)
                curr.pop(-1)

        subset = set()

        dfs(subset, [], nums, 0)

        return subset


