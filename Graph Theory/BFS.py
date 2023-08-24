""" 
Bu bölümde, bir yönlü graf yapısını temsil eden bir sözlük tanımlanıyor. Her düğüm ("A", "B", vb.) bir anahtar olarak temsil ediliyor ve bu düğümlerin komşuları kümeler halinde saklanıyor. Örneğin, "A" düğümünün komşuları "B" ve "C" olarak belirtilmiş.
"""

graph = {
    "A": set(["B", "C"]),
    "B": set(["A", "D", "E"]),
    "C": set(["A", "F"]),
    "D": set(["B"]),
    "E": set(["B", "F"]),
    "F": set(["C", "E"])
}

print(graph)

def bfs(graph, start):
    visited = set()     # Ziyaret edilen düğümleri takip etmek için bir küme oluşturuyoruz.
    queue = [start]     # Kuyruk (queue) başlangıç düğümüyle başlatılıyor.

    while queue:        # Kuyruk boş olana kadar devam ediyoruz.
        vertex = queue.pop(0)  # Kuyruğun başındaki düğümü çıkarıyoruz (BFS'te en eski eklenen önce gezilir).
        if vertex not in visited:   # Düğüm daha önce ziyaret edilmediyse:
            visited.add(vertex)     # Düğümü ziyaret edildi olarak işaretliyoruz (kümeye ekliyoruz).
            # Düğümün komşularını (ziyaret edilmemiş olanları) kuyruğa ekliyoruz.
            queue.extend(graph[vertex] - visited)

    return visited  # Ziyaret edilen düğümlerin kümesini döndürüyoruz.

""" 
İlk olarak, "visited" kümesi boş bir şekilde başlatılır. Bu küme ziyaret edilen düğümleri takip eder.
"queue" kuyruğu başlangıç düğümüyle başlatılır. Bu düğümden başlayarak tüm komşuları sırayla gezilecektir.
Kuyruk boş olana kadar döngü devam eder.
Kuyruğun başındaki düğüm çıkarılır (pop(0) ile çıkarılır çünkü BFS'te en eski eklenen önce gezilir).
Eğer çıkarılan düğüm daha önce ziyaret edilmediyse:
Düğümü "visited" kümesine ekleriz (ziyaret edildi olarak işaretleriz).
Düğümün komşularından ziyaret edilmemiş olanları ("visited" kümesinde olmayanları) kuyruğa ekleriz.
Son olarak, tüm işlem tamamlandığında "visited" kümesini döndürürüz, bu da gezilen düğümleri temsil eder.
"""
# 
print(bfs(graph, "A"))