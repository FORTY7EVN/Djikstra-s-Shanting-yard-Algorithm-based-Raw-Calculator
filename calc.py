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


# Convert an infix mathematical expression into one numeric result.
def calculate(expression: str):
    # Store the numbers and operators extracted from the expression.
    tokens = []
    # Store operators temporarily while processing the expression.
    op_stack = []
    # Store the resulting postfix tokens in evaluation order.
    output_queue = []
    # Remove spaces so tokenization can process the expression uniformly.
    equation = expression.replace(" ", "")
    # Accumulate consecutive digits as one number token.
    number = ""
    # List the symbols recognized by the tokenizer.
    symbols = {"+", "-", "*", "/", "^", "(", ")"}

    # Examine each character in the cleaned expression.
    for char in equation:
        # Append digits and decimal points to the current number.
        if char.isdigit() or char == ".":
            number += char
        # Handle an operator or parenthesis as a separate token.
        elif char in symbols:
            # Finish the number before adding the symbol.
            if number != "":
                # Convert decimal text to float and integer text to int.
                tokens.append(float(number) if "." in number else int(number))
                # Reset the number buffer for the next token.
                number = ""
            # Add the operator or parenthesis to the token list.
            tokens.append(char)
        else:
            # Reject characters that are not part of a supported expression.
            raise ValueError(f"Invalid character: {char}")

    # Add a number that appears at the end of the expression.
    if number != "":
        # Convert the final number to the appropriate numeric type.
        tokens.append(float(number) if "." in number else int(number))

    # Process each token according to the shunting-yard algorithm.
    for token in tokens:
        # Numbers go directly into the output queue.
        if token not in symbols and type(token) in (int, float):
            output_queue.append(token)
        # Opening parentheses wait on the operator stack.
        elif token == "(":
            op_stack.append(token)
        # Closing parentheses flush operators until the matching opening one.
        elif token == ")":
            # Move operators inside the parentheses to the output queue.
            while op_stack and op_stack[-1] != "(":
                output_queue.append(op_stack.pop())
            # Reject a closing parenthesis without a matching opening one.
            if not op_stack:
                raise ValueError("Mismatched parentheses: extra ')'")
            # Discard the matching opening parenthesis.
            op_stack.pop()
        # Process a recognized operator using precedence and associativity.
        elif token in OPS:
            # Keep the current operator separate for readability.
            operator = token
            # Move higher- or equally-precedent operators to the output queue.
            while (
                op_stack
                and op_stack[-1] != "("
                and (
                    (
                        OPS[operator]["assoc"] == "L"
                        and OPS[operator]["prec"]
                        <= OPS[op_stack[-1]]["prec"]
                    )
                    or (
                        OPS[operator]["assoc"] == "R"
                        and OPS[operator]["prec"]
                        < OPS[op_stack[-1]]["prec"]
                    )
                )
            ):
                # Pop the operator that should be evaluated first.
                output_queue.append(op_stack.pop())
            # Store the current operator until its operands are available.
            op_stack.append(operator)

    # Empty the remaining operator stack after all tokens are processed.
    while op_stack:
        # An opening parenthesis left here has no matching closing parenthesis.
        if op_stack[-1] == "(":
            raise ValueError("Mismatched parentheses: extra '('")
        # Append the remaining operator to the postfix output.
        output_queue.append(op_stack.pop())

    # Evaluate the postfix expression and return its single numeric result.
    value_stack = []
    for token in output_queue:
        # Numbers are saved until an operator needs them.
        if type(token) in (int, float):
            value_stack.append(token)
        # Operators consume the two most recent values.
        elif token in OPS:
            # Reject operators that do not have two operands.
            if len(value_stack) < 2:
                raise ValueError("An operator is missing an operand")
            # Pop the right operand before the left operand.
            right = value_stack.pop()
            left = value_stack.pop()

            # Apply the operator to its operands.
            if token == "+":
                value = left + right
            elif token == "-":
                value = left - right
            elif token == "*":
                value = left * right
            elif token == "/":
                value = left / right
            else:
                value = left ** right

            # Save the intermediate result for the next operator.
            value_stack.append(value)
        else:
            # Reject any unexpected token in the postfix expression.
            raise ValueError(f"Invalid postfix token: {token}")

    # A complete expression must leave exactly one result.
    if len(value_stack) != 1:
        raise ValueError("The expression does not produce a single result")

    # Return the completed calculation.
    return value_stack[0]


# Run the calculator when this file is executed directly.
if __name__ == "__main__":
    expression = input("Enter an equation: ")
    print(calculate(expression))
