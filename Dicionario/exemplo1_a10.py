import os

os.system('cls')

# EXEMPLO 1

lista = []

dicionario = {}

# CHAVE - VALOR
dicionario = {
    'nome' : 'João',
    'telefone' : '90028922',
    'idade' : 25,
    'cpf' : '111.222.333-44'
}

# exibindo valores
# ALT + SHIFT + BAIXO/CIMA: Duplica linhas
# ALTA + Baixo/Cima: Move linhas
print(dicionario['nome'])
print(dicionario['telefone'])
print(dicionario['idade'])
print(dicionario['cpf'])

# Alterando valores
dicionario['nome'] = 'Sonic'
print(dicionario['nome'])

# Adicionando valores
dicionario['email'] = 'joao@gmail.com'
print(dicionario['email'])

# Deletando valores
del dicionario['email']
print(dicionario)

# Deletando valores com POP (Retorna o valor da chave apagada)
print(dicionario.pop('idade', 'Idade não encontrada'))
print(dicionario.pop('email', 'Email não encontrado'))
