from node import Node

class Line:
    def __init__(self):
        self.head = None
        self.size = 0

    def enqueue(self, elem):
        self.size += 1
        node = Node()
        node.name = elem

        if(self.head is None):
            self.head = node
        else:
            current = self.head
            while(current.next):
                current = current.next
            
            current.next = node
            

    def dequeue(self):
        self.size -= 1
        if(self.head is None):                      # Primeiro verificamos se a lista está vazia
            print("A Lista está vazia")
        else:
            current = self.head                     # Salvo o antigo head com o nome e o ponetiro
            self.head = current.next                # Reatribuimos o self.head fazendo referencia ao ponteiro para o segundo item da lista
        
        
    
    def get_size(self):
        print(self.size)

    def imprimir(self):
        current = self.head
        if(self.head is None):
            print("A lista está vazia")
        else:
            while(current):
                print(current.name)
                current = current.next
