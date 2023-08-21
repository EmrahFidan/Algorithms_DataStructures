def bubble_sort(array):
    array_length = len(array)
    
    # Döngü dizinin tamamı sıralanana kadar devam eder
    for pass_num in range(array_length - 1, 0, -1):
        # Her döngüde, dizinin elemanları arasında sıralama yapılır
        for i in range(pass_num):
            current_item = array[i]
            next_item = array[i + 1]
            
            # Eğer şu anki eleman, bir sonraki elemandan büyükse yer değiştirilir 
            if current_item > next_item:
                array[i], array[i + 1] = array[i + 1], array[i]
    
    return array

# Kullanım örneği
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print("Sırasız liste:", unsorted_list)

sorted_list = bubble_sort(unsorted_list)
print("Sıralı liste:", sorted_list)
