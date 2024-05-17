def buscaBinaria(seq, valor):
    ini = 0
    fim = len(seq) - 1
    while(fim >= ini):
        meio = (ini + fim) // 2
        print(ini)
        print(fim)
        print(meio)
        if (seq[meio] == valor):
            return f"True, indice {meio}"
        elif (seq[meio] < valor):
            ini = meio + 1
        else:
            fim = meio - 1
        print("----------------")
    return False

lista = [1,2,3,4,5,6,7,8,9]
resp = buscaBinaria(lista, 8)
print(resp)

# Busca binária possui O(log n) como desempenho