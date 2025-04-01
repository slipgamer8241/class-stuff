"""
infix_to_postfix.py
Author: Marcus Sweet
Date: 2025.03.31
This script converts infix expressions to postfix expressions . 
It supports interactive mode for single expressions and file mode for batch processing. 
Key features include operator precedence, parentheses handling, and error detection for mismatched parentheses. 
Results are saved to 'test_results.txt' in file mode. Usage: Run without arguments for interactive mode 
or provide a file with infix expressions as an argument.
"""

import sys
from csarray import Stack


def is_operator(c):
    """
    Checks if a given character is a mathematical operator or parenthesis.
    """
    return c in ['+', '-', '*', '/', '(', ')', '^']


def precedence(op):
    """
    Determines the precedence of a given operator.

    Args:
        op (str): The operator whose precedence is to be determined. 
                  Supported operators are '+', '-', '*', '/', and '^'.

    Returns:
        int: The precedence level of the operator. Higher values indicate higher precedence.
             Returns 1 for '+' and '-', 2 for '*' and '/', 3 for '^', and 0 for unsupported operators.
    """
    if op in ['+', '-']:
        return 1
    elif op in ['*', '/']:
        return 2
    elif op == '^':
        return 3
    else:
        return 0


def infix_to_postfix(expression):
    """
    Converts an infix expression to a postfix expression.

    Args:
        expression (str): The infix expression as a string. The expression can contain
        alphanumeric operands, operators (+, -, *, /, ^), and parentheses.

    Returns:
        str: The postfix expression as a string if the conversion is successful.
        If there are mismatched parentheses, returns an error message:
        "Error: Mismatched parentheses".
    """
    stack = Stack()  # Stack to hold operators and parentheses
    postfix = []  # List to store the postfix expression
    for char in expression:
        if char.isalnum():  # If the character is an operand
            postfix.append(char)
        elif char == '(':  # If the character is a left parenthesis
            stack.push(char)
        elif char == ')':  # If the character is a right parenthesis
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            if not stack.is_empty() and stack.peek() == '(':
                stack.pop()
            else:
                return "Error: Mismatched parentheses"
        else:  # If the character is an operator
            while (not stack.is_empty() and stack.peek() != '(' and
                   precedence(char) <= precedence(stack.peek())):
                postfix.append(stack.pop())
            stack.push(char)

    # Pop remaining operators from the stack
    while not stack.is_empty():
        top = stack.pop()
        if top == '(' or top == ')':
            return "Error: Mismatched parentheses"
        postfix.append(top)

    return ''.join(postfix)


def main():
    """
    Converts infix expressions to postfix. Supports:
    1. Interactive Mode: Input a single expression and get the result.
    2. File Mode: Process expressions from a file, save results, and provide a summary.
    Handles errors and logs failed conversions.
    """
    if len(sys.argv) == 1:
        # Interactive mode
        expression = input("Enter infix expression: ")
        print("Postfix expression:", infix_to_postfix(expression))
    elif len(sys.argv) == 2:
        # File mode
        file_name = sys.argv[1]
        total_tests = 0
        passed_tests = 0
        failed_tests = 0
        failed_details = []

        try:
            with open(file_name, 'r') as file:
                expressions = file.readlines()
            with open('test_results.txt', 'w') as output_file:
                for line in expressions:
                    line = line.strip()
                    # Skip empty lines and comments
                    if line and not line.startswith('#'):
                        sub_expressions = line.split()
                        for expression in sub_expressions:
                            total_tests += 1
                            postfix = infix_to_postfix(expression)
                            if "Error" in postfix:  # Handle errors
                                failed_tests += 1
                                failed_details.append(
                                    f"Infix: {expression} -> Error: {postfix}")
                            else:
                                passed_tests += 1
                                output_file.write(
                                    f"Infix: {expression}\nPostfix: {postfix}\n\n")

                # Write summary to the output file
                output_file.write(f"Total Tests: {total_tests}\n")
                output_file.write(f"Passed Tests: {passed_tests}\n")
                output_file.write(f"Failed Tests: {failed_tests}\n\n")
                if failed_tests > 0:
                    output_file.write("Failed Details:\n")
                    for detail in failed_details:
                        output_file.write(f"{detail}\n")

            # Print summary to the console
            print("Test results saved to test_results.txt")
            print(f"Total Tests: {total_tests}")
            print(f"Passed Tests: {passed_tests}")
            print(f"Failed Tests: {failed_tests}")
            if failed_tests > 0:
                print("Failed Details:")
                for detail in failed_details:
                    print(detail)

        except FileNotFoundError:
            print(f"File {file_name} not found.")
    else:
        print("Usage: python infix_to_postfix.py [test_file.txt]")


if __name__ == "__main__":
    main()
