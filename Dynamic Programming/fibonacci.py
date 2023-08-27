def fibonacci(n):
    fib = [0, 1]  # The first two Fibonacci numbers
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])  # Sum of the previous two numbers
    return fib[n]

n = int(input("Which term of the Fibonacci series would you like to calculate? "))
result = fibonacci(n)
print(f"The {n}th term of the Fibonacci series: {result}")


""" 
# Recursive

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = int(input("Which term of the Fibonacci series would you like to calculate? "))
result = fibonacci_recursive(n)
print(f"The {n}th term of the Fibonacci series: {result}")

"""