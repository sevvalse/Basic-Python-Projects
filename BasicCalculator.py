while 1:
    print("Hi! Please choose a menu.\n1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif choice == "2":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif choice == "3":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif choice == "4":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        while 1:
            if num2 == 0:
                print("Please enter different number!")
                num2 = int(input("Enter second number: "))
            elif num2 != 0:
                break
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Please choose a valid menu option!")
