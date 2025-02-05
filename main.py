from Minus import Minus
from Mul import Mul
from Num import Num
from Plus import Plus
from Div import Div



"1 + ( 3*5 )"
def shunting_yard(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operators = []
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
    for token in tokens:
        if token.isdigit():
            output.append(Num(int(token)))
        elif token in precedence:
            while operators and operators[-1] != '(' and precedence[operators[-1]]>= precedence[token]:
                output.append(operators.pop())
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()
    while operators:
        output.append(operators.pop())
    return output

def build_expression_tree(postfix):
    stack = []
    for token in postfix:
        if isinstance(token, Num):
            stack.append(token)
        else:
            right = stack.pop()
            left = stack .pop()
            if token == '+':
                stack.append(Plus(left, right))
            elif token == '-':
                stack.append(Minus(left, right))
            elif token == '*':
                stack.append(Mul(left, right))
            elif token == '/':
                stack.append(Div(left, right))
    return stack.pop()

def parse_expression(expression):
    postfix = shunting_yard(expression)
    tree = build_expression_tree(postfix)
    return tree.calc()


if __name__ == "__main__":
    expr = "10 *  4 + (5 - 3)"
    result = parse_expression(expr)
    print(f"Result of '{expr}' is {result}")












