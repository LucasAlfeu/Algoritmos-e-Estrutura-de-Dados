from node import Node

# Criando os nós

nA = Node("A")
nB = Node("B")
nC = Node("C")
nD = Node("D")
nE = Node("E")
nF = Node("F")
nG = Node("G")
nH = Node("H")

# Criando a arvore

nA.left_child = nB
nA.right_child = nC
nB.left_child = nD
nB.right_child = nE
nC.right_child = nF
nD.left_child = nG
nD.right_child = nH

# Travessia da Árvore

# 1 Travessia In Order(subarvore esquerda -> raiz -> subarvore direita)

def inorder(root_node):
    current = root_node
    if(current is None):
        return
    inorder(current.left_child)
    print(current.data)
    inorder(current.right_child)

#Saída -> G D H B E A C F

#inorder(nA)

# 2 Travessia Pre Order (raiz -> subarvore esquerda -> subarvore direita) 

def preorder(root_node):
    current = root_node
    if(current is None):
        return
    print(current.data)
    preorder(current.left_child)
    preorder(current.right_child)

#Saída -> A B D G H E C F 

#preorder(nA)

# 3 Tavessia Post-Order (subarvore esqueda -> subarvore direita -> raiz)

def postorder(root_node):
    current = root_node
    if(current is None):
        return
    postorder(current.left_child)
    postorder(current.right_child)
    print(current.data) 

#Saída -> G H D E B F C A

#postorder(nA)