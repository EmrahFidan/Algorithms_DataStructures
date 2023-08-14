""" 
# ikili arama

-> ikili arama algoritması, sıralı bir dizide arama yapmak için kullanılan bir arama algoritmasıdır.
-> divide and conquer ( böl ve fethet) mantığı ile çalışır. 
-> O(log n) -> en kötü durum

Bir düşün, senin bir sürü sayı arasında özel bir sayıyı bulman gerekiyor. Ama bu sefer sayılar sıralı bir şekilde, yani küçükten büyüğe doğru dizilmiş. İşte "Binary Search" dediğimiz şey, bu tür durumda özel bir sayıyı hızlıca bulman için kullandığın bir yöntem.

Sadece 2 adımda nasıl çalıştığını gösteriyorum:

Adım 1: Ortadan Başla
İlk önce sayıları en ortasından ikiye ayırıyorsun. Bu sayede listenin ortasındaki sayıya bakıyorsun. Eğer aradığın sayı bu ortadaki sayıya eşitse, işlem tamam! Sayıyı buldun ve mutlu bir şekilde kullanabilirsin.

Adım 2: Eşleşme Kontrolü ve İkiye Bölme
Eğer ortadaki sayı aradığın sayı değilse, burası önemli. Şimdi ikiye ayırdığın bu listeden hangi yarıya bakacağına karar vermelisin. Eğer aradığın sayı, ortadaki sayıdan daha küçükse, yani solda ise, sağdaki yarısını tamamen göz ardı edebilirsin. Eğer aradığın sayı, ortadaki sayıdan daha büyükse, yani sağda ise, soldaki yarısını göz ardı edebilirsin.

Bu ikiye ayırma ve kontrol adımlarını devam ettirerek aradığın sayıya yaklaşacaksın.

Bu yöntemi tekrarlayarak, her seferinde sayıları yarıya böler ve aradığın sayıya yaklaşırsın. En sonunda, sayıyı bulursun ve sevinçle kullanabilirsin!
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Kullanıcıdan hedef değeri al
target_value = int(input("Hedef değeri giriniz: "))

my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18]
result = binary_search(my_list, target_value)

if result != -1:
    print(f"Hedef değer {target_value} bulundu, indeks: {result}")
else:
    print(f"Hedef değer {target_value} bulunamadı.")
