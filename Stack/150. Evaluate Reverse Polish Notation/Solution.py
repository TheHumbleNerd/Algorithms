class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opMap = {
                    '+': (lambda x,y: x+y),
                    '-': (lambda x,y: x-y),
                    "*": (lambda x,y: x*y),
                    "/": (lambda x,y: int(x/y))
                }
        
        st = []
        result = 0
        for i in tokens:
            if i in opMap:
                v1 = int(st.pop())
                v2 = int(st.pop())
                result = opMap[i](v2, v1)
                st.append(result)
            else:
                st.append(i)
        
        return int(st[-1])
