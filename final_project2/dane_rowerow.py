import requests
import pandas as pd

# Function for downloading from  CKAN API using SQL queries
def fetch_data_sql(sql):
    url = 'https://www.wroclaw.pl/open-data/api/action/datastore_search_sql'
    params = {'sql': sql}
    response = requests.get(url, params=params)
    response.raise_for_status()  # check for errors
    return response.json()

if __name__ == '__main__':
    # squel query to download data from 2023-11-05
    sql_query = "SELECT * FROM \"c737af89-bcf7-4f7d-8bbc-4a0946d7006e\" WHERE \"Data wynajmu\" >= '2023-11-05' AND \"Data wynajmu\" < '2023-11-06'"

    # downloading data
    data = fetch_data_sql(sql_query)
    records = data['result']['records']

    # Converting to DataFrame
    df = pd.DataFrame.from_records(records)

    # Changing columns
    df = df[['Data wynajmu'] + [col for col in df.columns if col != 'Data wynajmu']]

    # Saving DataFrame to CSV file
    df.to_csv('dane_rowerowe_2023-11-05.csv', index=False)

    print('Downloaded data and saved to file named dane_rowerowe_2023-11-05.csv')
