
def reverse(string):
    
    # base case
    if len(string) <= 1:
        return string
    
    # recursion case
    return reverse(string[1:]) + string[0]

text = input("Enter a string: ")

print("Reversed string:", reverse(text))
