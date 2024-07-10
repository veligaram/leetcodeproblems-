class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        move = 0
        for operation in logs:
            if operation == "../":
                move -= 1 if move > 0 else 0
            elif operation == "./":
                pass
            else:
                move += 1
        return move