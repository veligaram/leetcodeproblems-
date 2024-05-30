class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # https://www.youtube.com/watch?v=DwvNIVLcT8U
        res, hashmap, cur = 0, defaultdict(list), 0
        for i, ele in enumerate(arr):
            cur ^= ele
            if cur == 0:
                res += i
            if cur in hashmap:
                for after in hashmap[cur]:
                    res += (i - after - 1)
            hashmap[cur] += [i]
        return res