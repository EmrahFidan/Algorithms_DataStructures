def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Diziyi ikiye böleriz
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Her yarım diziyi ayrı ayrı sıralarız
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Sıralanmış yarım dizileri birleştiririz
    sorted_arr = merge(left_half, right_half)
    
    return sorted_arr

def merge(left, right):
    """
    İki sıralı diziyi birleştirerek yeni bir sıralı dizi oluşturur.
    
    Returns:
    list: İki yarım dizinin birleştirilmiş sıralı hali.
    """
    result = []
    left_index, right_index = 0, 0
    
    # İki yarım diziyi karşılaştırarak birleştiririz
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    # Eğer bir yarım dizi tamamlandıysa, diğer yarım dizinin kalanını sonuca ekleriz
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    
    return result

# Kullanım örneği
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print("Sırasız liste:", unsorted_list)

sorted_list = merge_sort(unsorted_list)
print("Sıralı liste:", sorted_list)
