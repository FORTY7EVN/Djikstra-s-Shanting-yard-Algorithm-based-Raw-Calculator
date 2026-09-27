input_var = None

operators = {
    "+": {"prec": 1, "assoc": "L"},
    "-": {"prec": 1, "assoc": "L"},
    "*": {"prec": 2, "assoc": "L"},
    "/": {"prec": 2, "assoc": "L"},
    "^": {"prec": 3, "assoc": "R"},
}

equation = input("Enter an expression: ")
if not equation:
    raise ValueError("No expression entered.")


def tokenize(expression: str):
    op_stack = []
    output_queue = []
    evaluation_stack = []
    equation = expression.replace(" ", "")
    tokens = []
    current_number = ""
    operators = {"+", "-", "*", "/", "^", "(", ")"}

    for char in equation:
        if char.isdigit() or char == ".":
            current_number += char
        elif char in operators:
            if current_number != "":
                if "." in current_number:
                    tokens.append(float(current_number))
                else:
                    tokens.append(int(current_number))
                current_number = ""
            tokens.append(char)

    if current_number != "":
        if "." in current_number:
            tokens.append(float(current_number))
        else:
            tokens.append(int(current_number))
    for token in tokens:
        if isinstance(token, (int, float)):
            output_queue.append(token)
        elif token in operators:
            op1 = token
            while (
                len(op_stack) > 0
                and
                op_stack[-1] != "("
                and
                (
                    (
                        operators[op1][assoc] == "L"
                        and
                        operators[op1]["prec"] <= operators[op_stack[-1]]["prec"]
                    )
                )
            )


print(tokenize(equation))
