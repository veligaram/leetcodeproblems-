class Solution:
    def pivotInteger(self, n: int) -> int:
        x = (n * (n + 1) / 2) ** 0.5
        if x % 1 != 0:
            return -1
        return int(x)