from ListaLinkada import Lista_Linkada

ingredientes = Lista_Linkada()
ingredientes.adicionar("Pão")
ingredientes.adicionar("Queijo")
ingredientes.adicionar("Presunto")
ingredientes.adicionar("Pão")


current = ingredientes.ini
while current:
    print(current.valor)
    current = current.prox

