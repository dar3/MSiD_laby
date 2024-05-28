from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os


def get_year_month_from_url(url):
    parts = url.split('/')
    year_month_str = parts[-1]
    year, month = map(str, year_month_str.split('-'))
    if len(month) < 2:
        month = '0' + month
    return month


def append_data_to_csv(data, filename):
    data.to_csv(filename, mode='a', index=False, header=not os.path.exists(filename))


def clear_csv_file(filename):
    open(filename, 'w').close()


def scrap_temp_humidity_wind(year):
    for n in range(1, 13):
        url_main = 'https://www.wunderground.com/history/monthly/pl/wroc%C5%82aw/EPWR/date/' + year + '-'
        url = url_main + str(n)
        print('Ściągamy: ', url)

        service = Service("C:\\chrome_driver\\chromedriver.exe")
        options = Options()
        driver = webdriver.Chrome(service=service, options=options)

        try:
            month = get_year_month_from_url(url)
            filename = 'thw_' + year + '.csv'
            data_file = Path(filename)
            if n == 1 and data_file.is_file():
                os.remove(data_file)
            driver.get(url)
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'table.days.ng-star-inserted'))
            )
            table_data = driver.execute_script("""
                let rows = document.querySelectorAll('table.days.ng-star-inserted tbody tr');
                let data = [];
                rows.forEach(row => {
                    let dateTable = row.querySelector('td:nth-child(1) table');
                    let tempTable = row.querySelector('td:nth-child(2) table');
                    let humidityTable = row.querySelector('td:nth-child(3) table');
                    let windTable = row.querySelector('td:nth-child(4) table');

                    if (dateTable && tempTable && humidityTable && windTable) {
                        let dateCells = dateTable.querySelectorAll('tr');
                        let tempCells = tempTable.querySelectorAll('tr');
                        let humidityCells = humidityTable.querySelectorAll('tr');
                        let windCells = windTable.querySelectorAll('tr');

                        dateCells.forEach((dateCell, index) => {
                            let dateText = dateCell.querySelector('td').innerText.trim();
                            let avgTempText = tempCells[index].querySelectorAll('td')[1].innerText.trim();
                            let avgHumidityText = humidityCells[index].querySelectorAll('td')[1].innerText.trim();
                            let avgWindText = windCells[index].querySelectorAll('td')[1].innerText.trim();
                            data.push([dateText, avgTempText, avgHumidityText, avgWindText]);
                        });
                    }
                });
                return data;
            """)

            if table_data:
                table_data = table_data[1:len(table_data)]
                for i in range(0, len(table_data)):
                    if len(table_data[i][0]) < 2:
                        table_data[i][0] = year + '-' + month + '-' + '0' + table_data[i][0]
                    else:
                        table_data[i][0] = year + '-' + month + '-' + table_data[i][0]

                df = pd.DataFrame(table_data, columns=['Date', 'Avg Temperature', 'Avg Humidity', 'Avg Wind Speed'])
            else:
                df = pd.DataFrame(columns=['Date', 'Avg Temperature', 'Avg Humidity', 'Avg Wind Speed'])

            append_data_to_csv(df, filename)
            print('Dane za rok ' + year + ' i miesiąc ' + month + ' zostały dodane')

        finally:
            print('Wszystkie dane zostały zapisane do pliku ', filename)
            driver.quit()


if __name__ == "__main__":
    scrap_temp_humidity_wind('2023')
