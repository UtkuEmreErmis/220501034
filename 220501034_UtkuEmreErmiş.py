import re
from collections import defaultdict
from heapq import *

class WordHeapNode: #Bir kelimenin ve onun sayısının saklandığı bir düğümü temsil eder.
    def __init__(self, word, count):
        self.word = word #Bu özellik, düğümün temsil ettiği kelimeyi saklar.
        self.count = count #Bu özellik, kelimenin metinde kaç kez geçtiğini saklar.

    def __lt__(self, other): #Bu metod, iki WordHeapNode örneğinin karşılaştırılmasını sağlar.
        if self.count == other.count:
            return self.word < other.word
        return self.count > other.count

def count_words(file_path): #Bir metindeki kelimelerin frekansını hesaplar.
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().lower()
    words = re.findall(r'\b\w+\b', text) #Metindeki tüm kelimeleri bulmak için kullanılır. \b\w+\b ifadesi, bir kelimenin başlangıcını ve sonunu belirler.
    word_count = defaultdict(int) #Bir sözlük oluşturulur. Bu sözlük, her kelimenin kaç kez geçtiğini saklar.
    for word in words:
        word_count[word] += 1
    return word_count

def heap_sort(word_count): #Bir kelime sayısı sözlüğünü alır ve her bir kelime ve sayı çifti için bir WordHeapNode oluşturur. Daha sonra, bu düğümleri bir yığın veri yapısına ekler.
    heap = []
    for word, count in word_count.items():
        heappush(heap, WordHeapNode(word, count)) #Bir öğeyi yığına ekler ve yığının özelliklerini korur.
    return [heappop(heap) for _ in range(len(heap))]

def print_word_counts(heap): #Bir WordHeapNode listesini alır ve her bir düğümün kelimesini ve sayısını yazdırır.
    for node in heap:
        print(f'{node.word}: {node.count}')

def main(): #Programın ana giriş noktasıdır ve diğer tüm fonksiyonları çağırır.
    file_path = input('Enter the path to the txt file: ')
    word_count = count_words(file_path)
    heap = heap_sort(word_count)
    print_word_counts(heap)

if __name__ == '__main__':
    main()
