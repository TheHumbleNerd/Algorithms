class Solution:

    def generationHelper(self, openCount: int, closedCount: int, n: int, s: str, result: List[str]):
        if openCount == n and closedCount == n:
            result.append(s)
        
        if openCount < n:
            s+= "("
            self.generationHelper(openCount+1, closedCount, n, s, result)
            s = s[:-1]
        
        if closedCount < openCount:
            s+= ")"
            self.generationHelper(openCount, closedCount+1, n, s, result)
            s = s[:-1]

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generationHelper(0, 0, n, "", result)
        return result
