class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtrack(openn, closee):
            if openn == closee == n:
                res.append("".join(stack))
                return
            if openn < n:
                stack.append("(")
                backtrack(openn + 1, closee)
                stack.pop()
            if closee < openn:
                stack.append(")")
                backtrack(openn, closee + 1)
                stack.pop()
        backtrack(0, 0)
        return res