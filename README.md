# Dijkstra's Shunting-Yard Calculator

A small command-line calculator that parses arithmetic expressions using the
shunting-yard algorithm and evaluates them in postfix (Reverse Polish) form.

## Requirements

- Python 3.6 or later

The calculator uses only the Python standard library; no packages need to be
installed.

## Run the Calculator

From the project directory, run:

```bash
python main.py
```

Enter one expression when prompted. For example:

```text
Enter a mathematical expression: (2 + 3) * 4
20
```

The command-line calculator displays up to four digits after the decimal point,
removing trailing zeroes. For example, `7 / 2` displays as `3.5`.

## Supported Expressions

The calculator supports:

- Whole numbers and decimal numbers, such as `12` and `3.5`
- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Exponentiation: `^`
- Parentheses for grouping
- Spaces between tokens

Examples:

```text
2 + 3 * 4       = 14
(2 + 3) * 4     = 20
7 / 2           = 3.5
2 ^ 3 ^ 2       = 512
```

Exponentiation is right-associative, so `2 ^ 3 ^ 2` is interpreted as
`2 ^ (3 ^ 2)`. The `^` symbol means exponentiation in this calculator.

## Operator Precedence

Operators are evaluated in this order, from highest precedence to lowest:

| Operators | Precedence | Associativity |
| --- | ---: | --- |
| `^` | 3 | Right |
| `*`, `/` | 2 | Left |
| `+`, `-` | 1 | Left |

Parentheses can be used to override the normal precedence.

## Python API

`calc.py` provides a function that accepts an expression string and returns its
numeric result:

```python
from calc import calculate

result = calculate("(2 + 3) * 4")
print(result)  # 20
```

Unlike the command-line display, `calculate()` returns the result without
rounding it to four decimal places.

## Errors and Limitations

- Division by zero is rejected by the command-line calculator.
- Mismatched parentheses and unsupported characters are rejected.
- Unary plus and minus are not supported, so expressions such as `-3` and
	`2 ^ -3` cannot currently be entered.
- Functions and other operations are not currently supported. This includes
	trigonometry, roots, factorial, percentages, permutations, and combinations.
- The calculator expects a complete arithmetic expression; it does not support
	implicit multiplication such as `2(3 + 4)`.

## Project Files

- `main.py` — interactive command-line calculator.
- `calc.py` — reusable `calculate(expression)` implementation.
