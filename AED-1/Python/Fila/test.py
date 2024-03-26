from line import Line

nome = Line()
print("Começaremos a fila")

def mostra_menu():
    print("")
    print("Menu")
    print("")
    print("1- Receber")
    print("2- Atender")
    print("3- Imprimir fila")
    print("")

while(True):
    mostra_menu()
    i = input("Insira um número: ")
    print("")
    match i :
        case "1":
            add = input("Insira seu nome: ")
            nome.append_first(add)
            print("")
        case "2":
            print("Atendendo...")
            nome.remove_first()
            print("")
        case "3":
            print("")
            print("Fila: ")
            nome.show_line()
            print("")