""" 
N'e kadar normal sayıları yaz bu algoritma asal sayıları oradan çeksin.

sieve = elek
"""

# Bir sayının asal olup olmadığını kontrol eden fonksiyon
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    # Asal sayılar 6k ± 1 formülüne uyar, bu nedenle sadece bu değerler kontrol edilir
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Belirli bir üst sınıra kadar olan asal sayıları bulan fonksiyon
def find_primes_up_to(limit):
    prime_list = []
    for num in range(2, limit + 1):
        if is_prime(num):  # Eğer bir sayı asalsa
            prime_list.append(num)  # Listeye ekle
    return prime_list

# Kullanıcıdan bir üst sınır girmesini iste
limit = int(input("Bir üst sınır girin: "))
# Belirli bir üst sınıra kadar olan asal sayıları bul
primes = find_primes_up_to(limit)
# Bulunan asal sayıları ekrana yazdır
print("Asal sayılar:", primes)
