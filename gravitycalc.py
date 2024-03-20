import pandas as pd

df = pd.read_csv('bright_stars.csv')

df['mass_kg'] = df['Mass'] * 1.989e+30

df['radius_m'] = df['Radius'] * 6.957e+8

def calculate_gravity(mass_kg, radius_m):
    G = 6.67430e-11  # gravitational constant in m^3 kg^-1 s^-2
    gravity = (G * mass_kg) / (radius_m ** 2)
    return gravity

gravity_values = []

for index, row in df.iterrows():
    gravity = calculate_gravity(row['mass_kg'], row['radius_m'])
    gravity_values.append(gravity)

df['gravity'] = gravity_values

print(df)
