import pandas as pd

# Passo 1: Importar a base de dados
tabela = pd.read_csv('telecom_users.csv')

# Passo 2: Visualizar a base de dados
#  - Entender as informações que você tem disponível
#  - Descobrir erros da base de dados
# print(tabela)


# Passo 3: Tratamento de dados
tabela = tabela.drop('Unnamed: 0', axis = 1)
print(tabela.info()) # mostrar as informações da tabela
tabela["TotalGasto"] = pd.to_numeric(tabela['TotalGasto'], erros="coerce") # converter os valores em números

# Passo 4: Análise inicial


# Passo 5: Análise detalhada - descobrir as causas do cancelamento
