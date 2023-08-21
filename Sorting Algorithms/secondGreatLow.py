def secondGreatLow(arr):
    unique = set(arr)
    # tekrar eden elemanları kaldırır.
    
    sortedList = sorted(unique)
    # sorted =>  Timsort, insertion sort ve merge sort gibi algoritmaların bir kombinasyonunu kullanarak verimli ve kararlı bir sıralama işlemi gerçekleştirir.
    
    if (len(sortedList) < 2):
        return str(sortedList[0]) 
    
    else:
        return str(sortedList[1]) + " " + str(sortedList[-2])
    
print(secondGreatLow([7, 1, 12, 98, 106]))