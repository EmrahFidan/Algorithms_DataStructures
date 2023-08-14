""" 
# Sıralı Arama

Bir kitaplığın içinde düzenli bir şekilde sıralanmış kitaplar olduğunu hayal et. Bu kitaplar isimlerine göre sıralanmış, yani A'dan Z'ye doğru gidiyorlar. Senin görevin, belirli bir kitabı bulmak için "Sequential Search with Ordered List" adını verdiğimiz yöntemi kullanmak.

İşte adım adım nasıl yapılacağını anlatıyorum:

Adım 1: Ortadan Başla
İlk adım olarak, kitapların en ortasındaki kitaba bakıyorsun. Eğer aradığın kitap bu kitap mı? Eğer öyleyse, işlem tamamlanmış demektir!

Adım 2: Eşleşme Kontrolü
Eğer ortadaki kitap aradığın kitap değilse, işte burası önemli. Eğer aradığın kitap ortadaki kitaptan daha önce (alfabetik sıraya göre) geliyorsa, o zaman kitapları yarısını kesip ikinci yarıyı göz ardı edebilirsin. Eğer aradığın kitap ortadaki kitaptan sonra geliyorsa, o zaman ilk yarıyı göz ardı edebilirsin.

Adım 3: İkiye Böl ve Devam Et
Bu şekilde adımları devam ettirerek, her seferinde kitapları yarıya bölebilirsin. Aradığın kitap ile karşılaşana kadar bu işlemi tekrar edersin.

Adım 4: Kitabı Bulana Kadar Devam Et
Kitapları yarıya bölerken, her seferinde aradığın kitaba yaklaşacaksın. En sonunda aradığın kitabı bulacaksın ve sevinçle okuyabileceksin!

"""

def ordered_sequential_search(arr, target):
    """
    :arr: Sıralı olmayan liste
    :target: Hedef aranan değer
    :return: Hedef bulunduysa indeksi, bulunamadıysa -1
    enumerate() fonksiyonu, bir diziyi veya başka bir yineleyiciyi dolaşırken hem öğeyi hem de bu öğenin indeksini elde etmek için kullanılır. Bu, genellikle döngülerde öğeleri ve indekslerini aynı anda kullanmanız gerektiğinde oldukça kullanışlıdır.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
        elif value > target:
            return -1  # Sıralı olmayan listenin geri kalanında da aramaya gerek yok
    return -1

# Kullanıcıdan hedef değeri al
target_value = int(input("Hedef değeri giriniz: "))

my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18]
result = ordered_sequential_search(my_list, target_value)

if result != -1:
    print(f"Hedef değer {target_value} bulundu, indeks: {result}")
else:
    print(f"Hedef değer {target_value} bulunamadı.")
