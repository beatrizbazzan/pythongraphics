import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./dataset/spotify_artists.csv')

df_grouped = data.groupby('name')['duration_ms'].sum()

df_top10 = df_grouped.nlargest(10)

plt.pie(df_top10, labels=df_top10.index, autopct='%1.1f%%')

plt.title('Top 10 Musicas por duração')

plt.show()
