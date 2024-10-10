import os

# ATIVIDADE 1

pessoas = {}

for i in range(1):
    os.system('cls')
    nome = input("Digite o nome: ")
    n1 = float(input("Digite a sua nota 1: "))
    n2 = float(input("Digite a sua nota 2: "))
    n3 = float(input("Digite a sua nota 3: "))
    n4 = float(input("Digite a sua nota 4: "))
    median = (n1 + n2 + n3 + n4)/4

# Cria um dicionario com os dados do usuario dentro do dicionario pessoas[nome]
    pessoas[nome] = {
        'Nota_1': n1,
        'Nota_2': n2,
        'Nota_3': n3,
        'Nota_4': n4,
        'Media' : median
    }

# print(pessoas)

for p in pessoas:
    print(f"Nome: {p}")
    print(f"Nota 1: {pessoas[p]['Nota_1']}")
    print(f"Nota 2: {pessoas[p]['Nota_2']}")
    print(f"Nota 3: {pessoas[p]['Nota_3']}")
    print(f"Nota 4: {pessoas[p]['Nota_4']}")
    print(f"Média: {pessoas[p]['Media']}")
