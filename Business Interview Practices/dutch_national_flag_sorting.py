""" 
0,1,2 lerden oluşan array'ı sort et ve yeni bir liste veya array yaratmadan linear time da yapmalısın.

"""
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    
def nationalFlag(arr):
    
    low = 0
    middle = 0
    high = len(arr) - 1
    
    while middle <= high:
        if arr[middle] == 0:
            swap(arr, low, middle)
            low += 1 
            middle += 1
        elif arr[middle] == 2:
            swap(arr, middle, high)
            high -= 1
            
        elif arr[middle] == 1:
            middle += 1
            
    return arr

print(nationalFlag([2,0,0,1,2,1]))
            