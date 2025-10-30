import plotly.express as px
import websocket
import json
import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dados = pd.read_csv ('student_data.csv', delimiter = ",")
df = pd.DataFrame (dados)

print (df)

# Verificar valores em falta em cada uma das colunas
valores_falta = df.isnull().sum()
print (valores_falta)
print ()

cols = ['sex', 'address', 'famsize', 'Mjob', 'Fjob', 'reason', 
        'guardian', 'schoolsup', 'famsup', 'paid', 'activities',
        'nursery', 'higher', 'internet', 'romantic'] # Colunas não numéricas

for coluna in cols:
    # Ver os valores únicos da coluna
    valores_unicos = dados [coluna].unique()
    print ("Valores únicos da coluna ", coluna, ": ",valores_unicos)
    i = 0
    for valor in valores_unicos:
        linhas = np.where (dados[coluna] == valor)
        dados.loc[dados[coluna] == valor, coluna] = i
        i += 1
    
    print (dados [coluna])






