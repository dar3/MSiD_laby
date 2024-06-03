import os
import pandas as pd

# Ścieżka do folderu zawierającego pliki .csv
folder_path = "wypozyczenia_2023"

# Inicjalizacja pustego DataFrame do przechowywania danych z wszystkich plików
combined_data = pd.DataFrame()

# Pętla przez wszystkie pliki w folderze
for filename in os.listdir(folder_path):
    if filename.endswith(".csv") and filename.startswith("Historia_przejazdow_2023"):
        # Wczytaj plik .csv do DataFrame
        file_path = os.path.join(folder_path, filename)
        data = pd.read_csv(file_path)
        # Dodaj dane do połączonego DataFrame
        combined_data = pd.concat([combined_data, data], ignore_index=True)

# Zapisz połączone dane do nowego pliku .csv
combined_data.to_csv("bikes_merged.csv", index=False)

print("Pomyślnie połączono i zapisano dane.")
