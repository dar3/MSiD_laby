import requests
from bs4 import BeautifulSoup
import csv

# URL strony, którą chcemy zeskrobać
url = 'https://dar3.eu/'

# Pobierz stronę
response = requests.get(url)

# Sprawdź, czy pobranie się powiodło
if response.status_code == 200:
    page_content = response.text
    # Parsuj stronę
    soup = BeautifulSoup(page_content, 'html.parser')

    # Wyodrębnij nagłówki
    headers = soup.find_all('h1')
    data = [header.text for header in headers]

    # Zapisz dane do pliku CSV
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Header'])
        for row in data:
            writer.writerow([row])
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
