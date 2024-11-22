while 1:
    n = int(input("Please enter a number: "))
    if n < 0:
        print("Factorial cannot be negative")
        continue
    result = 1
    for i in range(1, n+1):
        result *= i
    print(f"{n}! = {result}")
    break
