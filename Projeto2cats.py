import plotly.express as px
import websocket
import json
import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go

dados = pd.read_csv ('cat_breeds_clean.csv', delimiter = ";")
df = pd.DataFrame (dados)
print (df)

country_breed_sleep = df.groupby(['Country', 'Breed'], observed = False)['Sleep_time_hours'].mean().reset_index()
fig = px.scatter_geo (
    country_breed_sleep,
    locations = 'Country',
    locationmode = 'country names',
    color = 'Sleep_time_hours',
    size = 'Sleep_time_hours',
    hover_name = 'Breed',
    projection = 'natural earth',
    title = 'Horas médias de sono por raça de gato em cada país',
    hover_data = ['Sleep_time_hours']
)
fig.show()

gatos = {'Angora': "🐈‍⬛", 'Maine coon': "🐈", 'Ragdoll': "🐈‍⬛"}

# Média de sono por país
country_avg = df.groupby("Country")["Sleep_time_hours"].mean().reset_index()
country_avg.rename(columns={"Sleep_time_hours": "Avg_sleep"}, inplace=True)

# Criar figura
fig = go.Figure()

# Mapa coroplético por país
fig.add_trace(go.Choropleth(
    locations=country_avg["Country"],
    locationmode='country names',
    z=country_avg["Avg_sleep"],
    colorscale='Blues',
    colorbar_title="Média horas de sono"
))

# Adicionar barras verticais por raça usando as coordenadas reais
for i, row in df.iterrows():
    fig.add_trace(go.Scattergeo(
        lon=[row["Longitude"], row["Longitude"]],
        lat=[row["Latitude"], row["Latitude"] + row["Sleep_time_hours"] * 0.2],  # altura proporcional
        mode="lines",
        line=dict(width=10, color="red"),
        name=f"{row['Country']} - {row['Breed']}",
        hoverinfo='text',
        text=f"{row['Breed']}: {row['Sleep_time_hours']}h"
    ))

fig.update_layout(
    geo=dict(projection_type='natural earth'),
    title="Horas de sono por raça (barras) com média por país"
)

fig.show()

# Verificar valores em falta em cada uma das colunas
valores_falta = df.isnull().sum()
print (valores_falta)
print ()

cols = ['Breed', 'Gender', 'Neutered_or_spayed', 'Fur_colour_dominant', 
        'Fur_pattern', 'Eye_colour', 'Allowed_outdoor', 'Preferred_food', 'Country'] # Colunas não numéricas

for coluna in cols:
    # Ver os valores únicos da coluna
    valores_unicos = dados [coluna].unique()
    print ("Valores únicos da coluna ", coluna, ": ",valores_unicos)
    i = 0
    for valor in valores_unicos:
        linhas = np.where (dados[coluna] == valor)
        dados.loc[dados[coluna] == valor, coluna] = i
        i += 1
    
    #print (dados [coluna])






