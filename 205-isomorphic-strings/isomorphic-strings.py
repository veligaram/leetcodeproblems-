class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        map2 = {}
        for i in range(len(s)):
            if s[i] in map:
                if map[s[i]] != t[i]:
                    return False
            if t[i] in map2:
                if map2[t[i]] != s[i]:
                    return False
            else:
                map[s[i]] = t[i]
                map2[t[i]] = s[i]
        return True