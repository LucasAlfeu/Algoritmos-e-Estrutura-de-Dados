from No import No

class Lista_Linkada:
    def __init__(self):
        self.ini = None
        self._tamanho = 0

    def adicionar(self, elem):
        no = No(elem)                   # inicializa um novo nó
        if self.ini is None:            # testa pra ver se a lista está vazia
            self.ini = no
        else:
            atual = self.ini            # atual recebe o primeiro item da lista
            while (atual.prox):         # percorrer a lista para encontrar o ultimo elemento
                atual = atual.prox
            atual.prox = no
        
        self._tamanho = self._tamanho + 1 # incrementa os elementos tem na lista

    def __len__(self):
        return self._tamanho
    
    def __getitem__(self, index):
        atual = self.ini                # pegamos o primeiro item da lista
        for i in range(index):          # Iteramos a lista com o indexpassado
            if atual:                   # Se o atual existir então pegamos o proximo item da lista
                atual.prox
            else:
                raise IndentationError("list index out of range") # Se o atual não existir cai no erro
            
        if atual:                       # verifica se o atual não está vazio
            return atual.valor          # retornamos o valor de atual
        else:
            raise IndentationError("list index out of range")   # Se ele o atual não existir mostramos o erro
    
    def __setitem__(self, index, elem):
        atual = self.ini                # pegamos o primeiro item da lista
        for i in range(index):          # Iteramos a lista com o indexpassado
            if atual:                   # Se o atual existir então pegamos o proximo item da lista
                atual.prox
            else:
                raise IndentationError("list index out of range") # Se o atual não existir cai no erro
            
        if atual:                       # verifica se o atual não está vazio
            atual.valor = elem          # atualizamos o valor do atual
        else:
            raise IndentationError("list index out of range")   # Se ele o atual não existir mostramos o erro
        
    # def inserir_item_numa_posicao(self, index, elem):
    #     if(index > self._tamanho):
    #         self.adicionar(elem)
    #     else:
