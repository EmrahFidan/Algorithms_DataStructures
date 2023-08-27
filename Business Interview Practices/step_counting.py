""" 
n tane basamaklı bir merdivenden çıkmak istiyoruz, her bir step'de 2er veya 2 şer çıkabiliriz.
Ne kadar farklı şekilde çıkabiliriz.  
"""

def countStep(N):
    
    # base case 1
    if N == 1:
        return 1
    
    # base case 2
    if N == 2:
        return 2
    
    return countStep(N-1) + countStep(N-2)

print(countStep(8))
    