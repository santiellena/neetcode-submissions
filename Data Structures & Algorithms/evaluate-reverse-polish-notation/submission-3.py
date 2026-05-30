class Solution:
    

    def evalRPN(self, tokens: List[str]) -> int:
    
        def add(a, b) -> int:
            return a + b

        def sub(a, b) -> int:
            return a - b

        def mul(a, b) -> int:
            return a * b

        def div(a, b) -> int:
            return int(a / b)

        stack = []
        operations = {"+": add, "-": sub, "*": mul, "/": div}
        
        for token in tokens:
            print(stack)

            if token not in operations:
                stack.append(int(token))
            else:
                print(token)
                a = stack[-2]
                b = stack[-1]

                stack.pop()
                stack.pop()

                
                stack.append(operations[token](a, b))

        return stack[0]
