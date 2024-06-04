from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os


def get_year_month_from_url(url):
    parts = url.split('/')  # Division url on different parts
    year_month_str = parts[-1]  # Last part or url is month and year, that's why I use -1
    year, month = map(str, year_month_str.split('-'))  # Splitting data on month and year part
    if len(month) < 2:
        month = '0' + month
    return month  # Generating data list


def append_data_to_csv(data, filename):
    # Adding new data to csv file or create new file if not exist
    data.to_csv(filename, mode='a', index=False, header=not os.path.exists(filename))


def clear_csv_file(filename):
    # Clear csv file
    open(filename, 'w').close()


def scrap_temp_humidity_wind(year):
    for n in range(1, 13):
        # URL from which we scrap data for Wroclaw
        url_main = 'https://www.wunderground.com/history/monthly/pl/wroc%C5%82aw/EPWR/date/' + year + '-'
        url = url_main + str(n)
        print('Ściągamy: ', url)

        # Setting up Selenium WebDriver (you need to download chromedriver and give a path to it on your drive below)
        service = Service(
            "C:\\chrome_driver\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        try:
            month = get_year_month_from_url(url)
            # creating name for the file
            filename = 'thw_' + year + '.csv'

            data_file = Path(filename)
            if n == 1 and data_file.is_file():
                os.remove(data_file)

            # Opening webiste
            driver.get(url)

            # Giving some time to wait, so the page will be able to fully load
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'table.days.ng-star-inserted'))
            )

            # JavaScript code to be executed
            table_data = driver.execute_script("""
                let rows = document.querySelectorAll('table.days.ng-star-inserted tbody tr');
                let data = [];
                rows.forEach(row => {
                    let dateTable = row.querySelector('td:nth-child(1) table');
                    let tempTable = row.querySelector('td:nth-child(2) table');
                    // getting humidity level from 3 column
                    let humidityTable = row.querySelector('td:nth-child(3) table'); 
                    // getting wind speed  level from 4 column
                    let windTable = row.querySelector('td:nth-child(4) table'); 

                    if (dateTable && tempTable && humidityTable && windTable) {
                        let dateCells = dateTable.querySelectorAll('tr');
                        let tempCells = tempTable.querySelectorAll('tr');
                        let humidityCells = humidityTable.querySelectorAll('tr');
                        let windCells = windTable.querySelectorAll('tr');

                        dateCells.forEach((dateCell, index) => {
                            let dateText = dateCell.querySelector('td').innerText.trim();
                            // Aligned with 'Avg Temp' column
                            let avgTempText = tempCells[index].querySelectorAll('td')[1].innerText.trim(); 
                            // Aligned with 'Avg Humidity' column
                            let avgHumidityText = humidityCells[index].querySelectorAll('td')[1].innerText.trim(); 
                            // Aligned with 'Avg Wind' column
                            let avgWindText = windCells[index].querySelectorAll('td')[1].innerText.trim(); 
                            data.push([dateText, avgTempText, avgHumidityText, avgWindText]);
                        });
                    }
                });
                return data;
            """)

            # Creating DataFrame forom the data
            if table_data:
                table_data = table_data[1:len(table_data)]
                for i in range(0, len(table_data)):
                    if len(table_data[i][0]) < 2:
                        table_data[i][0] = year + '-' + month + '-' + '0' + table_data[i][0]
                    else:
                        table_data[i][0] = year + '-' + month + '-' + table_data[i][0]

                df = pd.DataFrame(table_data, columns=['Date', 'Avg Temperature', 'Avg Humidity', 'Avg Wind Speed'])
            else:
                df = pd.DataFrame(columns=['Date', 'Avg Temperature', 'Avg Humidity', 'Avg Humidity', 'Avg Wind Speed'])

            append_data_to_csv(df, filename)
            print('Dane za rok ' + year + ' i miesiąc ' + month + ' zostały dodane')

        finally:
            print('Wszystkie dane zostały zapisane do pliku ', filename)
            driver.quit()
