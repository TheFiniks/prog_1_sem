def calculate(postfix):
    try:
        stack = []
        for token in postfix:
            if token.isdigit():
                stack.append(token)
            elif token in ["-", "+", "*", "/"]:
                e2 = stack.pop()
                e1 = stack.pop()
                ans = str(eval(e1 + token + e2))
                stack.append(ans)
            else:
                return 'Error'
        if len(stack) == 1:
            return stack[0]
        else:
            return 'Error'
    except Exception:
        return 'Error'


postfix = input()
print(calculate(postfix))
