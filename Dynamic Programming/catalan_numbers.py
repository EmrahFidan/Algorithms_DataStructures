""" 
Katalan sayıları, kombinatorikte ve matematiksel analizde sıkça kullanılan bir sayı dizisidir. Bu sayılar, birçok farklı problemin çözümünde karşımıza çıkar ve özellikle parantezleme düzenlemeleri, ağaç yapıları, yol sayımları gibi alanlarda kullanılırlar.

C(0) = 1
C(n) = (2n * (2n - 1)) / ((n + 1) * n) * C(n - 1)

"""

def catalan_number(n):
    if n == 0:
        return 1
    
    catalan = [0] * (n + 1)
    catalan[0] = 1
    
    for i in range(1, n + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - j - 1]
    
    return catalan[n]

n = int(input("Which Catalan number would you like to calculate? "))
result = catalan_number(n)
print(f"The {n}th Catalan number: {result}")
