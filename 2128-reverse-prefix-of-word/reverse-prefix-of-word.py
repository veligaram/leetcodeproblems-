class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        prefix = ''
        for i, c in enumerate(word):
            if c == ch:
                return (prefix + c)[::-1] + word[i+1:]
            prefix += c
        return prefix