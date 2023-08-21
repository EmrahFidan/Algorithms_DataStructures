def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # Dizinin ortasındaki elemanı seçiyoruz
    left = [x for x in arr if x < pivot]  # Pivottan küçük elemanları sol listeye atarız
    middle = [x for x in arr if x == pivot]  # Pivota eşit olan elemanları orta listeye atarız
    right = [x for x in arr if x > pivot]  # Pivottan büyük elemanları sağ listeye atarız
    
    # Sol ve sağ listeleri tekrar quick_sort fonksiyonuna yollarız ve sonuçları birleştiririz
    return quick_sort(left) + middle + quick_sort(right)

# Kullanım örneği
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = quick_sort(unsorted_list)

print("Sırasız liste:", unsorted_list)
print("Sıralı liste:", sorted_list)
