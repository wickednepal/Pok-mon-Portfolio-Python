import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('pokemon.csv')

data = data[['Name', 'Type 1', 'Attack', 'Defense']]

data.dropna(inplace=True)

type_stats = data.groupby('Type 1')[['Attack', 'Defense']].mean()

type_stats_sorted = type_stats.sort_values(by='Attack', ascending=False)

print("Top 10 Types by Average Attack:")
print(type_stats_sorted.head(10))

type_stats_sorted.plot(kind='bar', figsize=(12,6))
plt.title('Average Attack and Defense by Pokémon Type')
plt.ylabel('Stat Value')
plt.xlabel('Pokémon Type')
plt.xticks(rotation=45)
plt.show()
