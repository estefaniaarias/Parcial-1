#A. Cargue los datos e identifique cuantas variables categóricas (tipo object) y cuantas variables numéricas tiene. 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('spotify-2023.csv', encoding ='latin-1')
print(df)

print(df.info())


# B. Desarrolle un algoritmo que nos diga cuantas canciones de Coldplay hay en la base de datos. 

canciones_coldplay = df[df['artist(s)_name'] == 'Coldplay'] 
num_canciones_coldplay = len(canciones_coldplay)
print(f'Canciones de Coldplay en la base de datos: {num_canciones_coldplay}')


# C. Encuentre el máximo y el mínimo de cada columna numérica en la base de datos. 

maximo = df.select_dtypes(include = ['number']).max()
print('Máximo de cada columna numérica:\n', maximo)

minimo = df.select_dtypes(include = ['number']).min()
print('Mínimo de cada columna numérica:\n', minimo)


# D. Desarrolle una función que reciba como parámetro su base de datos y un artista y le devuelva todas 
# las canciones de ese artista en base de datos. 

def canciones_artista(base_datos, artista):
    canciones = base_datos[base_datos['artist(s)_name'] == artista]
    return canciones
artista = 'Olivia Rodrigo'
canciones_olivia = canciones_artista(df, artista)

print(f'Las canciones de {artista} en la base de datos son:\n', canciones_olivia)


# E. Cree una tabla con una función de agregación, que muestre la sumatoria de cuantas 
#canciones Taylor Swift y Coldplay aparecen en playlist.

table = pd.pivot_table(data = df, index = 'artist(s)_name', values = 'track_name', aggfunc = 'count')
print('Tabla:\n', table.loc[['Taylor Swift' , 'Coldplay']])



#F. Desarrolle un subplot con dos gráficos, el primero es un boxplot relacione artist_count 
#(eje x) con streams, y el segundo un histograma de los años de lanzamiento.



df['artist_count'].unique() 
artistcount_streams = {}
for i in df ['artist_count'].unique():
    artistcount_streams[i] = df[df['artist_count'] == i]['streams']

[x for x in artistcount_streams.values()]
    
plt.boxplot([x for x in artistcount_streams.values()], labels=[x for x in artistcount_streams.keys()])
plt.xlabel('artist_count')
plt.ylabel('streams')
plt.title('BOXPLOT')


plt.hist(df['artist_count'], rwidth=0.5, color='purple')
plt.xlabel('artist_count')
plt.ylabel('streams')
plt.title('HISTOGRAMA')

plt.show()



