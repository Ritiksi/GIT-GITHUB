"""
This module performs simple calculator operations.
It asks user for input and prints the result.
"""


def simple_calculator():
    """
    Take user input for two numbers and an operator,
    then print the calculated result.
    """
    print("\n--- Welcome to Ritik's Calculator ---")

    try:
        num1 = float(input("Pehla number daalo: "))
        operator = input("Operator chunie (+, -, *, /): ")
        num2 = float(input("Dusra number daalo: "))

        if operator == '+':
            print(f"Result: {num1 + num2}")
        elif operator == '-':
            print(f"Result: {num1 - num2}")
        elif operator == '*':
            print(f"Result: {num1 * num2}")
        elif operator == '/':
            print(f"Result: {num1 / num2}")
        else:
            print("Bhai, operator sahi nahi hai!")

    except ValueError:
        print("Error: Number sahi se daalo bhai!")


# Run the function
if __name__ == "__main__":
    simple_calculator()
