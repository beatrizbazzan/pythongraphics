import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./dataset/spotify_artists.csv')

df_top10 = df.nlargest(10, 'danceability')

plt.scatter(df_top10['name'], df_top10['danceability'])

plt.xlabel('name')
plt.ylabel('danceability')

plt.title('Top Musicas por dançabilidade')

plt.show()
