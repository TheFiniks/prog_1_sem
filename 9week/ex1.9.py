Operators = '+-*/()^'
Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


def convert(string):
    exp = []
    for letter in string:
        if letter.isdigit():
            if exp[-1].isdigit():
                exp[-1] = exp[-1] + letter
            else:
                exp.append(letter)
        else:
            exp.append(letter)
    return exp


def infix_to_prefix(infix):
    stack = []
    ans = []
    for token in infix:
        if token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                ans.append(stack.pop() + str(ans.pop(-2)) + str(ans.pop()))
            stack.pop()
        elif token not in Operators:
            ans.append(token)
        else:
            while stack and stack[-1] != '(' and Priority[token] <= Priority[stack[-1]]:
                ans.append(stack.pop() + str(ans.pop(-2)) + str(ans.pop()))
            stack.append(token)
    while stack:
        ans.append(stack.pop() + str(ans.pop(-2)) + str(ans.pop()))
    return ''.join(ans)


def infix_to_postfix(infix):
    stack = []
    ans = []
    for token in infix:
        if token not in Operators:
            ans.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                ans.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and Priority[token] <= Priority[stack[-1]]:
                ans.append(stack.pop())
            stack.append(token)
    while stack:
        ans.append(stack.pop())
    return ''.join(ans)


infix = input()
# infix = '(2-3)*(12-10)+4/2'
# infix = '(3+4*(2-1))/5'
infix = convert(infix)
print(infix_to_prefix(infix))
print(infix_to_postfix(infix))
