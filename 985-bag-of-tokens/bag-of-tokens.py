class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if not tokens: return 0
        tokens.sort()
        score = 0
        if power < min(tokens): return 0
        left, right = 0, len(tokens)-1
        
        while left < right:
            if power >= tokens[left]:
                token = tokens[left]
                power -= token
                score += 1
                left += 1
            else:
                token = tokens[right]
                power += token
                score -=1
                right -=1
        
        return score + 1 if power >= tokens[right] else score

        