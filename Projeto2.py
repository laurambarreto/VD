import plotly.express as px
from sklearn.preprocessing import LabelEncoder
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

dados = pd.read_csv ('student_data.csv', delimiter = ",")
df = pd.DataFrame (dados)

print (df)

# Verificar valores em falta em cada uma das colunas
valores_falta = df.isnull().sum()
print (valores_falta)
print ()

cols = ['sex', 'address', 'famsize', 'Mjob', 'Fjob', 'reason', 
        'guardian', 'schoolsup', 'famsup', 'paid', 'activities',
        'nursery', 'higher', 'internet', 'romantic', 'Pstatus'] # Colunas não numéricas

# Converter todas para numéricas com LabelEncoder
le = LabelEncoder()

for col in cols:
    df[col] = le.fit_transform(df[col])
print(df)

# DataFrame df com todas as colunas numéricas
corr = df.corr(numeric_only = True)
plt.figure(figsize = (50, 20))
sns.heatmap(
    corr,
    annot = True,        # mostra os valores numéricos
    fmt = ".1f",         # arredonda para 2 casas decimais
    cmap = "coolwarm",   # cores azul/vermelho
    square = True,
    annot_kws = {"size": 6}      # tamanho da fonte dos números

)
plt.title("Mapa de Correlação entre Todas as Variáveis", fontsize=16)
plt.show()

## -- Gráfico de barras das correlações com G3 --
# Ordenar correlações com G3
corr_with_G3 = corr['G3'].drop('G3').sort_values(ascending = False)
# Criar figura
plt.figure(figsize = (12,6))
plt.bar(corr_with_G3.index, corr_with_G3.values, color = 'pink', edgecolor = "black", linewidth = 0.5,  zorder = 2)
# Linha azul em y = 0
plt.axhline(0, color = 'black', linewidth = 0.8, linestyle = '-', zorder = 3)
# Grelha suave atrás das barras
plt.grid(True, axis = 'y', linestyle = '--', alpha = 0.7, zorder = 1)
plt.title("Correlação de cada variável com a nota final (G3)", fontsize = 16, pad = 15)
plt.ylabel("Coeficiente de Correlação", fontsize = 12)
plt.xticks(rotation = 45, ha = 'right')
plt.tight_layout()
plt.show()


# Evolução da nota final em função do tempo de estudo
# Agregar dados: contar quantas pessoas têm cada combinação studytime x failures
bubble_data = df.groupby(['studytime', 'failures']).size().reset_index(name = 'count')

plt.figure(figsize = (10,6))

# Scatter com tamanho proporcional ao número de pessoas
plt.scatter(
    bubble_data['studytime'], 
    bubble_data['failures'], 
    s = bubble_data['count']*30,  # tamanho da bolha (ajustar factor para ficar visualmente bom)
    color = 'pink', 
    alpha = 0.6, 
    edgecolor = 'black',
    zorder = 2
)

plt.title("Distribuição de falhas por horas de estudo", fontsize=16, pad=15)
plt.xlabel("Horas de estudo", fontsize=12)
plt.ylabel("Número de falhas", fontsize=12)
plt.xticks(range(1,5))  # se studytime for de 1 a 4
plt.yticks(range(0,4))  # se failures de 0 a 3
plt.ylim(-0.5, 3.5)
plt.grid(True, linestyle='--', alpha = 0.7, zorder = 1)
plt.tight_layout()
plt.show()

for coluna in cols:
    # Ver os valores únicos da coluna
    valores_unicos = dados [coluna].unique()
    print ("Valores únicos da coluna ", coluna, ": ",valores_unicos)
    i = 0
    for valor in valores_unicos:
        linhas = np.where (dados[coluna] == valor)
        dados.loc[dados[coluna] == valor, coluna] = i
        i += 1
    
    






