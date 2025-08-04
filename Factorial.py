while 1: 
    n = int(input("Please enter a number: "))  
    if n < 0: 
        print("Factorial cannot be negative")  
        continue  
    result = 1  # Initialize the result variable to 1 (since the factorial of 0 is 1)
    for i in range(1, n+1):  # Loop from 1 to n (inclusive)
        result *= i   # Multiply result by the current value of i to calculate the factorial
    print(f"{n}! = {result}")  
    break  # Exit the loop after calculating the factorial
