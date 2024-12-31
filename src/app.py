import pandas as pd
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# load the .env file variables
load_dotenv()

client_id = os.environ.get('myclient_id')
client_secret = os.environ.get('myclient_secret')
spotify = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id, client_secret))

# adele_id = '4dpARuHxo51G3z768sgnrY'
# artist_top_tracks contiene las canciones con más reproducciones del artista
result_adele = spotify.artist_top_tracks('4dpARuHxo51G3z768sgnrY')

# Se crea una lista con el top 10 de las canciones del artista seleccionado
data = [ ]
for track in result_adele['tracks'][:10]:
    data.append((track['name'], round((track['duration_ms']/60000),2), track['popularity']))
print(data)

# Se convierten los datos a un Dataframe
df = pd.DataFrame(data, columns=['Name', 'Duration', 'Popularity'])
print(df)

# Se ordenan las canciones por popularidad creciente e imprime el top 3
sorted_df = df.sort_values(by='Popularity', ascending=False, ignore_index=True)
print(sorted_df[['Name', 'Duration', 'Popularity']][0:3])

# Scatter plot de la popularidad y la duración
ax = df.plot.scatter(x='Popularity', y='Duration', c='DarkBlue')





