""" 
input = "011?0" , bu input benim metoduma girecek daha sonra soru işaretinin yerine hem 0 hem de 1 yazılılacak. 
output = "01110" , "01100"
"""

def pattern(str, arr):
    
    # if stirng is empty
    if len(str) == 0:
        return arr
    
    if str[0] == "0" or str[0] == "1":
        for i in range(0, len(arr)):
            arr[i].append(str[0])
            
    # str[0] == ?
    if str[0] == "?":
        length = len(arr)
        for i in range(0, length):
            temp = list(arr[i])
            arr.append(temp)
        for i in range(0, len(arr)):
            if i < len(arr)/2:
                arr[i].append("0")
            else:
                arr[i].append("1")
                
    return pattern(str[1:],arr)

print(pattern("011?0",[[]]))
            