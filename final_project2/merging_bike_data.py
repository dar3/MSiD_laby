import pandas as pd
import glob
import os

# Press the green button to run the script.
if __name__ == '__main__':

    # You must have folder named Data with all the CSV files in your project
    folder_path = 'Data'

    # Finding all .CSV files in our path
    csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

    # List for storing DataFrame data
    dfs = []

    # Iteration through all CSV files and loading (reading) them
    for file in csv_files:
        df = pd.read_csv(file)
        dfs.append(df)

    # Merging all DataFrames into one
    combined_df = pd.concat(dfs, ignore_index=True)

    # Converting column  'Data wynajmu' to datetime format
    combined_df['Data wynajmu'] = pd.to_datetime(combined_df['Data wynajmu'])

    # Taking only date (without time) from column 'Data wynajmu'
    combined_df['Data wynajmu'] = combined_df['Data wynajmu'].dt.date

    # Converting column 'Czas trwania' to number type (if it's not a number type)
    combined_df['Czas trwania'] = pd.to_numeric(combined_df['Czas trwania'], errors='coerce')

    # Grouping by column 'Data wynajmu', counting amount of rents for a day and computing a sum in 'Czas trwania'
    daily_rentals = combined_df.groupby('Data wynajmu').agg(
        {'UID wynajmu': 'size', 'Czas trwania': 'sum'}).reset_index()

    # Changing column name from 'UID wynajmu' to 'Ilość wynajmów'
    daily_rentals.rename(columns={'UID wynajmu': 'Ilość wynajmów'}, inplace=True)

    # Saving data to a new CSV file
    output_file = 'daily_rentals_with_duration.csv'
    daily_rentals.to_csv(output_file, index=False)

    print(f'Dane zostały zapisane do pliku {output_file}')
