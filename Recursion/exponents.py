
def recursive_exponent(base, power):
    if power == 0:
        return 1
    else:
        return base * recursive_exponent(base, power - 1)
    
base = int(input("Enter base: "))
power = int(input("Enter power: "))

print("Result: ", recursive_exponent(base, power))