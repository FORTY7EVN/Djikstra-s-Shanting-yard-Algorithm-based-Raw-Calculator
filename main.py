input_var = None
operation_stack = []
output_queue = []
evaluation_stack = []

operator_metadata = {
    "+": ["left", 1],
    "-": ["left", 1],
    "*": ["left", 2],
    "/": ["left", 2],
    "^": ["right", 3],
}

equation = input("Enter an expression: ")
if not equation:
    raise ValueError("No expression entered.")


def tokenize(expression: str):

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
    return tokens


print(tokenize(equation))
# Output: [5, '+', 6, '*', '(', 88, '*', 780, ')']
