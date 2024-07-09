from time import sleep

# O segredo do Selection Sort é que salvamos o 
# índice do menor número de dentro do array e depois
# fazemos um SWAP com o item do array que estamos comparando

def selection_sort(seq):
    n = len(seq)
    for i in range(n-1):
        indice_menor = i
        for j in range(i+1, n):
            print("Comparando "+str(seq[i])+" com o número "+str(seq[j]))
            if(seq[j]<seq[indice_menor]):                                               #Encontra o indice do menor e salva em uma variável
                print("Trocando o menor indice de "+str(indice_menor)+" para "+str(j))
                indice_menor = j                                                        #Salvamos o indice do do menor númeor
                sleep(1)                                                                #Damos uma pausa de 1 segundo
            print()
            sleep(3)                                                                    #Damos um tempo de 3 segundos
        if(indice_menor != i):                                                          # Quando o indice_menor for diferente do valor de i
            aux = seq[i]                                                                # Fazemos o swap, trocamos os elementos de lugar
            seq[i] = seq[indice_menor]
            seq[indice_menor] = aux
        print(seq)
        print()
        sleep(2)

lista = [3, 5, 2, 1, 6]
selection_sort(lista)