import requests
from bs4 import BeautifulSoup

# Web sayfasını getirmek için bir istek gönder
url = 'https://www.example.com'
response = requests.get(url)

# İsteğin başarılı olup olmadığını kontrol et
if response.status_code == 200:
    # HTML içeriğini analiz etmek için BeautifulSoup kullan
    soup = BeautifulSoup(response.content, 'html.parser')

    # İlgilendiğiniz veriyi bulmak için uygun etiketleri seçin
    # Örneğin, tüm başlıkları bulmak için:
    titles = soup.find_all('h1')

    # Bulunan başlıkları yazdır
    for title in titles:
        print(title.text)
else:
    print("Web sayfasına erişilemedi.")
