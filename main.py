OPS = {
    # Addition is left-associative and has the lowest precedence.
    "+": {"prec": 1, "assoc": "L"},
    # Subtraction is left-associative and has the lowest precedence.
    "-": {"prec": 1, "assoc": "L"},
    # Multiplication is left-associative and has higher precedence.
    "*": {"prec": 2, "assoc": "L"},
    # Division is left-associative and has higher precedence.
    "/": {"prec": 2, "assoc": "L"},
    # Exponentiation is right-associative and has the highest precedence.
    "^": {"prec": 3, "assoc": "R"},
}


def shunting_yard(expression: str):
    tokens = []
    op_stack = []
    output_queue = []
    equation = expression.replace(" ", "")
    number = ""
    symbols = {"+", "-", "*", "/", "^", "(", ")"}

    for char in equation:
        if char.isdigit() or char == ".":
            number += char
        elif char in symbols:
            if number != "":
                tokens.append(float(number) if "." in number else int(number))
                number = ""
            tokens.append(char)
        else:
            raise ValueError(f"Invalid character: {char}")
    if number != "":
        tokens.append(float(number) if "." in number else int(number))
    for token in tokens:
        if token not in symbols and type(token) in (int, float):
            output_queue.append(token)
        elif token == "(":
            op_stack.append(token)
        elif token == ")":
            while op_stack and op_stack[-1] != "(":
                output_queue.append(op_stack.pop())
            if not op_stack:
                raise ValueError("Mismatched parentheses")
            op_stack.pop()  # Remove the opening parenthesis
        elif token in OPS:
            operator = token
            while (op_stack and op_stack[-1] in OPS and
                   ((OPS[operator]["assoc"] == "L" and OPS[operator]["prec"] <= OPS[op_stack[-1]]["prec"]) or
                    (OPS[operator]["assoc"] == "R" and OPS[operator]["prec"] < OPS[op_stack[-1]]["prec"]))):
                output_queue.append(op_stack.pop())
            op_stack.append(token)

    while op_stack:
        if op_stack[-1] in ("(", ")"):
            raise ValueError("Mismatched parentheses")
        output_queue.append(op_stack.pop())
    values = []
    for token in output_queue:
        if type(token) in (int, float):
            values.append(token)
        elif token in OPS:
            b = values.pop()
            a = values.pop()
            if token == "+":
                values.append(a + b)
            elif token == "-":
                values.append(a - b)
            elif token == "*":
                values.append(a * b)
            elif token == "/":
                if b == 0:
                    raise ValueError("Division by zero")
                values.append(a / b)
            elif token == "^":
                values.append(a ** b)
        else:
            raise ValueError(f"Invalid token in postfix expression: {token}")
    if len(values) != 1:
        raise ValueError(
            "The expression could not be evaluated to a single value")
    return values[0]


def evaluate():
    expression = input("Enter a mathematical expression: ")
    return print(shunting_yard(expression))


evaluate()
