from node import Node

class Pilha:
    def __init__(self):
        self.head = None

    def push(self, elem):
        node = Node(elem)
        if self.head is None:
            self.head = node
        else:
            aux = self.head
            self.head = node
            node.next = aux

    def pop(self):
        if(self.head is None):
            print("A lista está vazia")
        else:
            old_head = self.head
            new_head = old_head.next
            self.head = new_head

    def peek(self):
        if(self.head is None):
            print("A lista está vazia")
        else:
            last = self.head
            print("Útimo item da Pilha:")
            print(last.data)

    def imprimir(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next           