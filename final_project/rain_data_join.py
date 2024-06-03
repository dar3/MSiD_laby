import pandas as pd

# Reading data from first file and choosing only column "prcp"
df1 = pd.read_csv('wunder_weather_rain.csv', usecols=['prcp'])

# Reading data from second file
df2 = pd.read_csv('scrapped_correct_units_weather.csv')

# Merging two datas by indexes
merged_df = pd.concat([df2, df1], axis=1)

# Changing the column name to more elegant
merged_df.rename(columns={'prcp': 'Precipitation'}, inplace=True)

# Saving merged data to a new file
merged_df.to_csv('full_weather.csv', index=False)

print("Files were successfully merged.")
