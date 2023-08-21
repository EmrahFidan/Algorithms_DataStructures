def heapify(arr, n, i):
    largest = i    # Başlangıçta en büyük eleman olarak root belirlenir
    left = 2 * i + 1
    right = 2 * i + 2

    # Sol çocuk varsa ve sol çocuk root'tan daha büyükse
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Sağ çocuk varsa ve sağ çocuk root'tan daha büyükse
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Eğer en büyük eleman root değilse
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]   # Elemanları değiştir
        heapify(arr, n, largest)   # Değiştirilen alt ağaçta heapify işlemi tekrar yapılır

def heap_sort(arr):
    n = len(arr)

    # Diziyi max heap haline getir
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Heap'tan elemanları çıkararak sırala
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # En büyük elemanı sondaki elemanla değiştir
        heapify(arr, i, 0)   # Yeniden max heap haline getir

    return arr

# Kullanım örneği
unsorted_list = [12, 11, 13, 5, 6, 7]
sorted_list = heap_sort(unsorted_list)

print("Sırasız liste:", unsorted_list)
print("Sıralı liste:", sorted_list)
