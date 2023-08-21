def shell_sort(array):
    n = len(array)
    gap = n // 2  # Başlangıçta kullanılacak aralığı belirleme

    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i

            # Alt diziyi aralıklara göre sıralama
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap

            array[j] = temp

        gap //= 2  # Aralığı daraltma

    return array

# Kullanım örneği
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = shell_sort(unsorted_list)

print("Sırasız liste:", unsorted_list)
print("Sıralı liste:", sorted_list)
