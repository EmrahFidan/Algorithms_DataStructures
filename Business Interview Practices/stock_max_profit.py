""" 
Size liste veriliyor ve bu listede şirketin fiyatlandırmaları bulunuyor. Bizim hedefimiz max kar elde etmek. 
Yani en ucuza alıp en pahalıya satmamız lazım.
Eğer kar elde edemediysen return = -1 
"""

def stockPrice(list):
    
    max_profit = -1
    
    buy_price = 0
    sell_price = 0
    
    change_buy_index = True
    
    # Lopp Through List
    for i in range(0,len(list)-1):
        # selling prise 
        sell_price = list[i+1]
        
        # curring price
        if change_buy_index:
            buy_price = list[i]
            
        if sell_price < buy_price:
            change_buy_index = True
            continue # no profit
        
        else: 
            temp_price = sell_price - buy_price # positive change (kar)
            
            if temp_price > max_profit:
                max_profit = temp_price
                
            change_buy_index = False
            
    return max_profit
        
    
# Test 

print(stockPrice([1,45,6,64,33,22,87,99]))

#

