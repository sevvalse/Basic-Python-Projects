while 1:  # Start an infinite loop to continuously prompt the user
    n = int(input("Please enter a number: "))  # Prompt the user to enter a number
    if n < 0:  # Check if the entered number is negative
        print("Factorial cannot be negative")  # Inform the user that factorial is not defined for negative numbers
        continue  # Skip the rest of the loop and prompt the user again
    result = 1  # Initialize the result variable to 1 (since the factorial of 0 is 1)
    for i in range(1, n+1):  # Loop from 1 to n (inclusive)
        result *= i   # Multiply result by the current value of i to calculate the factorial
    print(f"{n}! = {result}")  # Print the calculated factorial
    break  # Exit the loop after calculating the factorial
