from time import sleep

def insert_sort(seq):
    n = len(seq)
    for i in range(1,n):
        print("Looping: "+str(i))
        valor = seq[i]
        position = i
        while(position > 0 and valor < seq[position - 1]):
            print("Posição: "+str(position))
            seq[position] = seq[position - 1]
            position -= 1
            print(seq)
            sleep(3)
        seq[position] = valor
        sleep(1)
        print()
    print("------------------------------")
    return seq

lista = [5,2,7,1,3,4,9]
lista = insert_sort(lista)
print(lista)