class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
      set1=set(nums1)
      set2=set(nums2)
      res=list(set1 & set2)
      res.sort()
      return res[0] if res else -1
