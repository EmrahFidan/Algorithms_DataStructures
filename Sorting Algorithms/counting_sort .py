def counting_sort(arr):
    
    # Dizideki maksimum değeri bulup bir sayaç dizisi oluşturuyoruz.
    max_value = max(arr)
    count_array = [0] * (max_value + 1)
    
    # Dizideki her elemanın sayısını sayaç dizisinde kaydediyoruz.
    for num in arr:
        count_array[num] += 1
    
    # Sayaç dizisini kullanarak sıralanmış bir dizi oluşturuyoruz.
    sorted_array = []
    for i, count in enumerate(count_array):
        sorted_array.extend([i] * count)
    
    return sorted_array

# Kullanım örneği
unsorted_list = [4, 2, 2, 8, 3, 3, 1] 
sorted_list = counting_sort(unsorted_list) 

print("Sırasız liste:", unsorted_list)
print("Sıralı liste:", sorted_list)
