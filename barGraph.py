import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./dataset/spotify_artists.csv')

labels = data['artists_names']
values = data['popularity']

ordered_values = pd.DataFrame({'Aristas': labels, 'Popularidade': values}).sort_values(by='Popularidade', ascending=False)

top_n=30

top_values = ordered_values.head(top_n)

# Create graph
plt.bar(top_values['Aristas'] , top_values['Popularidade'])

plt.xlabel('Aristas')
plt.ylabel('Popularidade')
plt.title('Aristas mais populares segundo spotify')

plt.xticks(rotation=90)

# Show graph
plt.show()
