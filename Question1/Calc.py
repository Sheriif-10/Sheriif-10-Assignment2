while True:
    while True:
        try:
            num1 = float(input("Enter first number: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        operation = input("Enter operation (+, -, *, /): ").strip()

        if operation in ["+", "-", "*", "/"]:
            break

        print("Invalid operation.")

    if operation == "/" and num2 == 0:
        print("Cannot divide by zero.")
        continue

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    else:
        result = num1 / num2

    print("Result:", result)

    while True:
        again = input("Do you want to calculate again? (y/n): ").strip().lower()

        if again == "y" or again == "n":
            break

        print("Please enter y or n.")

    if again == "n":
        break