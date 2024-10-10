import os

# EXEMPLO 2

pessoas = {}

for i in range(2):
    os.system('cls')
    nome = input("Digite o nome: ")
    email = input("Digite o Email: ")
    idade = int(input("Digite a idade: "))
    cpf = input("Digite o CPF: ")

# Cria um dicionario com os dados do usuario dentro do dicionario pessoas[nome]
    pessoas[nome] = {
        'Email':email,
        'Idade':idade,
        'Cpf':cpf
    }

print(pessoas)
print(pessoas[nome]['Email'])
