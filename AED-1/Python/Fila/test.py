from line import Line

nome = Line()
print("Começaremos a fila")

def mostra_menu():
    print("")
    print("Menu")
    print("")
    print("1- Enqueue")
    print("2- Dequeue")
    print("3- Imprimir fila")
    print("4- size")
    print("")

while(True):
    mostra_menu()
    i = input("Insira um número: ")
    print("")
    match i :
        case "1":
            add = input("Insira seu nome: ")
            nome.enqueue(add)
            print("")
        case "2":
            print("Atendendo...")
            nome.dequeue()
            print("")
        case "3":
            print("")
            print("Fila: ")
            nome.imprimir()
            print("")
        case "4":
            print("")
            print("A fila tem: ")
            nome.get_size()
            print("")