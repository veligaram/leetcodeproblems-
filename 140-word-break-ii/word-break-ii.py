class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = defaultdict(list)

        def _wordBreak_topdown(s):
            """return list of word lists"""
            if not s:
                return [[]]  # list of empty list

            if s in memo:
                return memo[s]

            for endIndex in range(1, len(s) + 1):
                word = s[:endIndex]
                if word in wordSet:
                    for subsentence in _wordBreak_topdown(s[endIndex:]):
                        memo[s].append([word] + subsentence)
            return memo[s]

        _wordBreak_topdown(s)

        return [" ".join(words) for words in memo[s]]