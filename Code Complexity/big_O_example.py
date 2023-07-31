# #todo O(1) - Constant Time 

def constant_big_o(list):
    print(list[0])

constant_big_o([1,2,3,4,5,6,7,8,9,10]) 

#todo O(1) - Lineer Time 

def constant_big_o(list):
    for variable in list:
        print(list[0])
        
constant_big_o([1,2,3,4,5,6,7,8,9,10]) 

#todo O(1) - Cubic Time 

def constant_big_o(list):
    for variable_1 in list:
         for variable_2 in list:
             for variable_3 in list:    
                print(variable_1,variable_2,variable_3)
        
constant_big_o([1,2,3]) 

"-----------------------------------------------------------------------------------------------"

# ! Calculating Big - O

#? İnsignificant constant sayıları ihmal edilir.

#? O(n) = O(2n) =  O(n + 10) = O(4 + n)

#? O(n^2) = O(2n^2) = O(100n^2 + 5n + 8)

