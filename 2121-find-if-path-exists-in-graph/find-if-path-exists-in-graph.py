class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def union_by_rank(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if i == j:
            return
        if self.rank[i] < self.rank[j]:
            self.parent[i] = j
        elif self.rank[i] > self.rank[j]:
            self.parent[j] = i
        else:
            self.parent[i] = j
            self.rank[j] += 1

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union_by_rank(u, v)
        return uf.find(source) == uf.find(destination)