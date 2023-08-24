# adjaceny list

# Her bir düğümü temsil eden Vertex sınıfı
class Vertex:
    def __init__(self, key):
        self.id = key  # Düğümün kimliği
        self.connectedTo = {}  # Bu düğümün komşularını ve aralarındaki bağlantıları bir sözlük olarak tutar
        
    def addNeighbor(self, neighbor, weight=0):
        self.connectedTo[neighbor] = weight  # Düğümün komşularına, komşu düğümü anahtar ve isteğe bağlı ağırlık olarak ekler
        
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    
    def getConnections(self):
        return self.connectedTo.keys()  # Düğümün komşularının kimliklerini içeren bir anahtar koleksiyonu döndürür
    
    def getId(self):
        return self.id  # Düğümün kimliğini döndürür
    
    def getWeight(self, neighbor):
        return self.connectedTo[neighbor]  # Belirli bir komşu düğüme olan bağlantının ağırlığını döndürür
    
    
# Tüm grafi yöneten Graph sınıfı
class Graph:
    def __init__(self):
        self.vertList = {}  # Grafa ait düğümleri kimlikleriyle ilişkilendiren bir sözlük
        self.numVertices = 0  # Toplam düğüm sayısını tutar
        
    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)  # Yeni bir düğüm oluşturur
        self.vertList[key] = newVertex  # Oluşturulan düğümü grafa ekler
        return newVertex
        
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]  # Belirli bir düğümü döndürür
        else:
            return None
        
    def __contains__(self, n):
        return n in self.vertList  # Bir düğümün grafa ait olup olmadığını kontrol eder
    
    def addEdge(self, fromVert, toVert, cost=0):
        if fromVert not in self.vertList:
            self.addVertex(fromVert)  # Eğer başlangıç düğümü graf içinde yoksa, ekler
            
        if toVert not in self.vertList:
            self.addVertex(toVert)  # Eğer hedef düğümü graf içinde yoksa, ekler
            
        self.vertList[fromVert].addNeighbor(self.vertList[toVert], cost)  # Başlangıç düğümüne bir komşu ekler
        
    def getVertices(self):
        return self.vertList.keys()  # Grafa ait tüm düğüm kimliklerini içeren bir anahtar koleksiyonu döndürür
    
    def __iter__(self):
        return iter(self.vertList.values())  # Graf içindeki tüm düğümleri sırayla döndürmek için yineleyici döndürür

graph = Graph()

graph.addVertex(1)
graph.addVertex(2)
graph.addVertex(3)
graph.addVertex(4)
graph.addVertex(5)
graph.vertList

graph.addEdge(1, 2,0)
graph.addEdge(1, 3,0)
graph.addEdge(5, 3,0)

for v in graph:
    print(v)
    print(v.getConnections())
    print('\n')