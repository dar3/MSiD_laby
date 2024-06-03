import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv("merged_data.csv")

    # Conversion from Fahrenheit to Celsius
    df["Avg Temperature"] = (df["Avg Temperature"] - 32) * 5 / 9

    # Converting wind speed from mp/h to km/h
    df["Avg Wind Speed"] *= 1.60934

    # Data rounding and converting small minus values of -0.0004 to 0
    df["Avg Temperature"] = df["Avg Temperature"].round().replace(-0, 0)
    df["Avg Wind Speed"] = df["Avg Wind Speed"].round().replace(-0, 0)

    # Changing to more elegant name
    df = df.rename(columns={"prcp": "Precipitation"})

    # All converted data was saved to new file
    df.to_csv("all_converted_data_old.csv", index=False)

    print("Dane zostały przekształcone i zapisane w nowym pliku.")
