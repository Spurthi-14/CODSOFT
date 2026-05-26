def calculator():
    print("Simple Calculator")
    print("Operations: + (add), - (subtract), * (multiply), / (divide)")
    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        print("\nChoose operation:")
        print("1. + (Addition)")
        print("2. - (Subtraction)")
        print("3. * (Multiplication)")
        print("4. / (Division)")
        operation = input("Enter your choice ('1' or '2' or '3' or '4' or '+' or '-' or '*' or '/' ): ").strip()
        if operation in ['1', '+']:
            result = num1 + num2
            op_symbol = '+'
        elif operation in ['2', '-']:
            result = num1 - num2
            op_symbol = '-'
        elif operation in ['3', '*']:
            result = num1 * num2
            op_symbol = '*'
        elif operation in ['4', '/']:
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
                return
            result = num1 / num2
            op_symbol = '/'
        else:
            print("Error: Invalid operation choice!")
            return
        print(f"\nResult: {num1} {op_symbol} {num2} = {result}")
    except ValueError:
        print("Error: Please enter valid numbers!")
if __name__ == "__main__":
    calculator()