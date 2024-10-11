import pandas as pd
import os

os.system('cls')

# EXEMPLO 3 - PANDAS
dados = {
    'cargos': ["assistente", "auxiliar", "gerente"],
    'salarios': [2500,1800,750]
}

dados_bi=pd.DataFrame(dados)
# print(dados_bi)

# SERIES

dados_cargos = pd.Series(dados["cargos"])
print(dados_cargos)

# INDICES E VALORES

print(dados_cargos.index)

print(dados_cargos.values)

# Impprime a linha do indice
df_linha = dados_bi.iloc[1]
# loc mais indicado para rotulos em textos
#df_linha = dados_bi.loc['cargos']

print(df_linha)

# Acessando valores individualmente
df_iloc = dados_bi.loc[0]['cargos']
print(df_iloc)
