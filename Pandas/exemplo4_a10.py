import pandas as pd
import os

# EXEMPLO 4 - LEITURA DE ARQUIVOS
try:
    os.system('cls')
    df_base_de_dados = pd.read_csv('ClassicDisco.csv',sep=",",encoding="utf-8")
    
    # Imprimindo a base de dados completa
    # TO STRING imprime tudo, enquanto o metodo simples resume.
    # O metodo head imprime so o cabecalho/numeros definidos.
    # Tail exibe só o final

    # print(df_base_de_dados.to_string())
    # print(df_base_de_dados)
    # print(df_base_de_dados.head(20))
    # print(df_base_de_dados.tail(10))

    # Imprime informaoes e resumo da base
    # print(df_base_de_dados.info())
    print(df_base_de_dados.describe())

except Exception as e:
    print(f"Erro {e}")
