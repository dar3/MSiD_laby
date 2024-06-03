import pandas as pd

# Wczytanie danych z pliku CSV
df = pd.read_csv("bikes_merged.csv")

# Konwersja kolumn "Data wynajmu" i "Data zwrotu" na typ daty
df["Data wynajmu"] = pd.to_datetime(df["Data wynajmu"])
df["Data zwrotu"] = pd.to_datetime(df["Data zwrotu"])

# Sortowanie danych według kolumn "Data wynajmu" i "Data zwrotu"
df_sorted = df.sort_values(by=["Data wynajmu", "Data zwrotu"])

# Zapis posortowanych danych do nowego pliku CSV
df_sorted.to_csv("bikes_merged_sorted.csv", index=False)

print("Dane zostały posortowane i zapisane w nowym pliku.")
