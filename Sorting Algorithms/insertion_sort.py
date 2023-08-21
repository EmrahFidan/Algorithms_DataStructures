def insertion_sort(array):
    for i in range(1, len(array)):
        # Şu anki elemanı geçici bir değişkende sakla
        current_item = array[i]
        j = i - 1
        
        # Şu anki elemandan daha büyük olan elemanları kaydır ve boşluğa yerleştir
        while j >= 0 and array[j] > current_item:
            array[j + 1] = array[j]
            j -= 1
        
        # Boşluğa şu anki elemanı yerleştir
        array[j + 1] = current_item
    
    return array

# Kullanım örneği
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print("Sırasız liste:", unsorted_list)

sorted_list = insertion_sort(unsorted_list)
print("Sıralı liste:", sorted_list)
