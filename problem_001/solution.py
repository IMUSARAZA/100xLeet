def solveMeFirst(a, b):
    return a + b

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    res = solveMeFirst(num1, num2)
    print(res)
except ValueError:
    print("Please enter valid integers.")