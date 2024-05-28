import pandas as pd

# Funkcja do konwersji Fahrenheita na Celsjusza
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def miles_ph_to_kilometers_ph(mph):
    return (mph * 1.609)

# Wczytaj plik CSV
df = pd.read_csv('thw_2023.csv')

# Conversion from Fahrenheit to Celsius
df['Avg Temperature'] = df['Avg Temperature'].apply(fahrenheit_to_celsius)
df['Avg Temperature'] = df['Avg Temperature'].round()

# change from -0 to 0 so that data would be normal
df['Avg Temperature'] = df['Avg Temperature'].apply(lambda x: 0 if x == -0.0 else x)

# Conversion from mph to km/h
df['Avg Wind Speed'] = df['Avg Wind Speed'].apply(miles_ph_to_kilometers_ph)
df['Avg Wind Speed'] = df['Avg Wind Speed'].round()





# Zapisz zaktualizowane dane do nowego pliku CSV
df.to_csv('scrapped_correct_units_weather.csv', index=False)

print("Temperatura została pomyślnie zamieniona na Celsjusza a mile na godzine zamieniono na km/h i zapisano nowe dane.")


