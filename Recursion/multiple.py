
def recursive_multiply(x, y):
    if x == 0 or y == 0:
        return 0
    if x == 1:
        return y
    if y == 1:
        return x
    return x + recursive_multiply(x, y - 1)

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

print("Product:", recursive_multiply(number1, number2))