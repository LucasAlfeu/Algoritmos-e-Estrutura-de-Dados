from linked_list import Linked_List

lista = Linked_List()

#lista.find(6)

lista.append(123)
lista.append(56)
lista.append(78)
lista.append(390)
lista.append(47)
lista.append(5)

atual = lista.head
while(atual):
    print(atual.data)
    atual = atual.next

# print("--------------------------")
# lista.find(2)
#print("--------------------------")
lista.modify(4, "Vasco")
print("--------------------------")

atual = lista.head
while(atual):
    print(atual.data)
    atual = atual.next