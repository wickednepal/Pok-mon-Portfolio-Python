import pandas as pd

data = pd.read_csv(r'C:\Users\prabe\Desktop\Portfolio\Pokemon.csv')

print(data.head())

# Keep only Type 1 column
types = data['Type 1']

# Count how many Pokémon per type
type_counts = types.value_counts()

# Print the result
print("Number of Pokémon per Type:")
print(type_counts)
