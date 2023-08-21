def selection_sort(array):
    
    array_length = len(array)
    
    # Döngü, dizinin tamamı sıralanana kadar devam eder
    for i in range(array_length - 1):
        # Minimum elemanın indisini saklamak için bir değişken oluşturulur
        min_index = i
        
        # Minimum elemanın indisi aranır
        for j in range(i + 1, array_length):
            if array[j] < array[min_index]:
                min_index = j
        
        # Minimum eleman bulunduğu indexteki elemanla yer değiştirilir
        array[i], array[min_index] = array[min_index], array[i]
    
    return array

# Kullanım örneği
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = selection_sort(unsorted_list)

print("Sırasız liste:", unsorted_list)
print("Sıralı liste:", sorted_list)
