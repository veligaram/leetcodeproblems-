import heapq
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(wage)
        workers = [(wage[i]/quality[i], quality[i]) for i in range(n)]
        workers.sort()
        total_quality = 0
        ratio = 0
        heap = []
        heapq.heapify(heap)
        for i in range(k):
            ratio = workers[i][0]
            total_quality += workers[i][1]
            heapq.heappush(heap, -workers[i][1])
        res = ratio*total_quality
        for i in range(k, n):
            ratio = workers[i][0]
            total_quality += workers[i][1]
            heapq.heappush(heap, -workers[i][1])
            quality = -heapq.heappop(heap)
            total_quality -= quality
            res = min(res, ratio*total_quality)
        return res