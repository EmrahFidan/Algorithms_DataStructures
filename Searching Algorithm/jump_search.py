""" 
# Zıplama Arama Algoritması

= Zıplama Arama Algoritması , sıralı bir dizideki bir öğeyi bulmak için kullanılan bir arama algoritmasıdır.
= O (√n) ->  yani en kötü durumda O (n) 'ye yaklaşır.


-> Düşün ki senin bir sürü not defterin var ve bu defterlerdeki sayfalar sıralı bir şekilde numaralandırılmış. Özel bir sayfayı hızlıca bulmak istiyorsun. İşte "Jump Search" dediğimiz yöntem, böyle bir durumda istediğin sayfayı bulmanı sağlayan bir yöntem.

Basitçe anlatıyorum:

Adım 1: Uzun Atlamayla Başla
İlk önce büyük adımlarla sayfaları atlayarak ilerlemeye başlıyorsun. Örneğin, ilk başta her 5 sayfa arasında bir atlayabilirsin. Yani 5. sayfadan başlayarak 10. sayfaya, 15. sayfaya gibi ilerlersin.

Adım 2: Küçük Atlamaya Geç
Bir noktada, istediğin sayfanın yakınına geldiğinde, adımlarını küçültüyorsun. Mesela, son 5 sayfaya geldiğinde tek tek her sayfayı kontrol ederek aradığın sayfayı bulmaya çalışıyorsun.

Bu yöntemle büyük adımlarla başlayıp, yaklaştıkça adımları küçültüyorsun.

Adım 3: Sayfayı Bulana Kadar Devam Et
Küçük adımlarla yaklaşırken, en sonunda aradığın sayfayı bulacaksın. Sayfayı bulduğunda sevinçle istediğin bilgiyi alabilirsin!
"""

import math

def jump_search(list, target):
    
    n = len(list)
    step = int(math.sqrt(n))
    prev = 0

    while list[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    while list[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1

    if list[prev] == target:
        return prev
    return -1

# Kullanıcıdan hedef değeri al
target_value = int(input("Hedef değeri giriniz: "))

my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18]
result = jump_search(my_list, target_value)

if result != -1:
    print(f"Hedef değer {target_value} bulundu, indeks: {result}")
else:
    print(f"Hedef değer {target_value} bulunamadı.")
