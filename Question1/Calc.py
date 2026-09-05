while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        print("Invalid operation.")
        continue

    print("Result:", result)

    again = input("Do you want to calculate again? (y/n): ")

    if again.lower() != "y":
        break