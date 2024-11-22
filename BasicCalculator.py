while 1:  # Start an infinite loop
    print("Hi! Please choose a menu.\n1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Exit")
    choice = input("Enter your choice: ")  # Prompt the user to enter their choice
    if choice == "1":  # Check if the user chose addition
        num1 = int(input("Enter first number: "))  # Get the first number from the user
        num2 = int(input("Enter second number: "))  # Get the second number from the user
        result = num1 + num2  # Calculate the sum
        print(f"{num1} + {num2} = {result}")  # Display the result
    elif choice == "2":  # Check if the user chose subtraction
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif choice == "3":  # Check if the user chose multiplication
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif choice == "4":  # Check if the user chose division
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        while 1:  # Start an inner infinite loop to ensure valid input for division
            if num2 == 0:  # Check if the second number is zero
                print("Please enter different number!")  # Prompt user to enter a non-zero number
                num2 = int(input("Enter second number: "))
            elif num2 != 0:  # If the second number is valid (non-zero)
                break  # Exit the inner loop
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    elif choice == "5":  # Check if the user chose to exit
        print("Goodbye!")  # Print a goodbye message
        break  # Exit the outer loop
    else:  # If the user input is not valid
        print("Please choose a valid menu option!")  # Prompt user to select a valid option
