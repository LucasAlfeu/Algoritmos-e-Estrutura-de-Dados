def bubbleSort(seq):
    n = len(seq)
    for i in range(n-1):
        for j in range(n-1-i):
            if(seq[j] > seq[j+1]):
                aux = seq[j]
                seq[j] = seq[j+1]
                seq[j+1] = aux
            print(seq)
        print("---------------------------------------------")
    return seq

lista = [99,3,57,100,2,10,67,45,-23]
print("-------------------------------------------------")
print(lista)
print("-------------------------------------------------")
lista = bubbleSort(lista)
print("--------------------------------------------------")
print(lista)