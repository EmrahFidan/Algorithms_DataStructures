def recursionBinarySearch(lst, element, start=0):
    # base case
    if len(lst) == 0:
        return False, None
    
    # recursive case
    else:
        mid = len(lst) // 2
        
        # if match found 
        # base case
        if lst[mid] == element:
            return True, start + mid
        
        else:
            if element < lst[mid]:
                return recursionBinarySearch(lst[:mid], element, start)
            else:
                return recursionBinarySearch(lst[mid+1:], element, start + mid + 1)

# Ask the user to input a sorted list
input_list = [4, 9, 12, 66, 94, 121, 45]
sorted_list = sorted(input_list)

# Ask the user to input an element to search for
element = int(input("Enter the element to search for: "))

# Perform binary search and print the result
found, index = recursionBinarySearch(sorted_list, element)
if found:
    print(f"Element found at index {index}!")
else:
    print("Element not found.")
