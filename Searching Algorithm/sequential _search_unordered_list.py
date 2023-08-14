# Sıralı Arama 
"""
-> O(n) -> en kötü durum 

= Senin bir sürü oyuncak arasında özel bir oyuncak bulman gerekiyor. Ama oyuncaklar rastgele yerlere dağıtılmış, yani bir düzenleri yok. İşte "Sequential Search with Unordered List" dediğimiz şey de böyle bir durumda oyuncaklar arasında istediğin özel oyuncak bulmak için yaptığın bir yöntem.Bunu şöyle düşünebilirsin: Her bir oyuncak kutuların içine rastgele atılmış ve kutuların üstünde numaralar yok. Senin görevin, kutuları sırayla tek tek açarak içine bakmak ve aradığın özel oyuncakla eşleşip eşleşmediğini kontrol etmek.

İşte adım adım nasıl yapacağını anlatıyorum:

Adım 1: İlk Kutudan Başla
İlk önce 1. kutuya gidiyorsun ve içine bakıyorsun. Eğer aradığın özel oyuncak bu kutuda ise, işlem tamam! Buldun demektir ve sevinçle oyuncakla oynayabilirsin.

Adım 2: Eşleşmezse, Bir Sonraki Kutuya Git
Eğer 1. kutuda aradığın oyuncak değilse, üzülme. Sıradaki kutuya geçiyorsun, yani 2. kutuya. İçine bakıyorsun, bakalım aradığın oyuncak burada mı?

Adım 3: Devam Et
Bu şekilde tek tek kutulara bakarak ilerliyorsun. Eğer aradığın oyuncak bir kutuda bulunana kadar bu adımları tekrar ediyorsun.

Adım 4: Bulana Kadar Devam Et
Kutuların içini kontrol ederken, aradığın oyuncakla eşleşene kadar bu işlemi tekrar ediyorsun. Eğer sonunda özel oyuncaklı bir kutu bulursan, hemen sevinçle çıkartıp oynayabilirsin!
"""

def unordered_linear_search(arr, target):
    """
    Düzensiz Liste ile Sıralı Olmayan Arama

    arr: Düzensiz liste
    target: Hedef aranan değer
    """
    for value in arr:
        if value == target:
            return True
    return False

# Kullanıcıdan hedef değeri al
target_value = int(input("Hedef değeri giriniz: "))

my_list = [34, 12, 9, 67, 23, 51, 87, 3]
found = unordered_linear_search(my_list, target_value)

if found:
    print(f"Hedef değer {target_value} bulundu.")
else:
    print(f"Hedef değer {target_value} bulunamadı.")
