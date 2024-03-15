from node import Node

class Linked_List:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, elem):
        node =  Node(elem)

        if(self.head is None):
            self.head = node
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = node
        self.size += 1

    def find(self, index):
        if(self.head is None):
            raise IndentationError("A lista está vazia")
        elif (self.size < index):
            raise IndentationError("Não possui numero na posição passada")
        else:
            current = self.head
            aux = 1
            while(aux < index):
                current = current.next
                aux += 1
            print(current.data)
    
    def modify(self, index, elem):
        if(self.head is None):
            raise IndentationError("A lista está vazia")
        elif (self.size < index):
            raise IndentationError("Não possui numero na posição passada")
        else:
            current = self.head
            aux = 1
            while(aux < index):
                current = current.next
                aux += 1
            current.data = elem