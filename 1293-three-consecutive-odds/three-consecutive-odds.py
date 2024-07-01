class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        listy = []
        for i in range(len(arr)-2):
            if arr[i]%2==1 and arr[i+1]%2==1 and arr[i+2]%2==1:
                listy.append(arr[i])
                listy.append(arr[i+1])
                listy.append(arr[i+2])
                break
        return listy