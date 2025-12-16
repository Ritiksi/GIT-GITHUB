def simple_calculator():
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


# Run the function (Upar 2 lines ka gap zaroori hai)
simple_calculator()
