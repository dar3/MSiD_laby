import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

if __name__ == '__main__':

    # Reading data
    data = pd.read_csv('all_converted_data.csv')

    # Viewing data to check visually how it looks
    print(data.head())
    print("test data")

    # Basic descriptive statistics
    print(data.describe())

    # Showing data summary to check for correctness of data types and missing values
    print(data.info())

    # Chart of the number of rented bikes depending on the temperature
    plt.scatter(data['Avg Temperature'], data['Ilość wynajmów'], alpha=0.5)
    plt.title('Liczba wypożyczonych rowerów vs. Temperatura')
    plt.xlabel('Średnia temperatura')
    plt.ylabel('Liczba wypożyczonych rowerów')
    plt.show()

    # Chart of the number of rented bikes depending on humidity
    plt.scatter(data['Avg Humidity'], data['Ilość wynajmów'], alpha=0.5)
    plt.title('Liczba wypożyczonych rowerów vs. Wilgotność')
    plt.xlabel('Średnia wilgotność')
    plt.ylabel('Liczba wypożyczonych rowerów')
    plt.show()

    # Chart of the number of rented bikes depending on wind speed
    plt.scatter(data['Avg Wind Speed'], data['Ilość wynajmów'], alpha=0.5)
    plt.title('Liczba wypożyczonych rowerów vs. Prędkość wiatru')
    plt.xlabel('Średnia prędkość wiatru')
    plt.ylabel('Liczba wypożyczonych rowerów')
    plt.show()

    # Chart of the number of rented bikes depending on amount of rainfall
    # text in [] after data takes name of our table heading
    plt.scatter(data['Precipitation'], data['Ilość wynajmów'], alpha=0.5)
    plt.title('Liczba wypożyczonych rowerów vs. Opady')
    plt.xlabel('Suma opadów')
    plt.ylabel('Liczba wypożyczonych rowerów')
    plt.show()

    # Selection of independent variables (features)
    X = data[['Avg Temperature', 'Avg Humidity', 'Avg Wind Speed', 'Precipitation']]

    # Selection of the dependent variable (number of rented bicycles)
    y = data['Ilość wynajmów']

    # Division of data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialization and starting training our model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predicting the number of rented bikes on test data
    y_pred = model.predict(X_test)

    # Model evaluation
    print('Mean Squared Error:', mean_squared_error(y_test, y_pred))
    print('Coefficient of Determination (R^2):', r2_score(y_test, y_pred))

    # Visualisation of the comparison of actual and predicted values and adding labels to charts
    plt.scatter(y_test, y_pred)
    plt.xlabel('Rzeczywista liczba wypożyczonych rowerów')
    plt.ylabel('Przewidywana liczba wypożyczonych rowerów')
    plt.title('Porównanie rzeczywistych i przewidywanych wartości')

    # Regression coefficients
    print('Współczynniki regresji:')
    for i, coef in enumerate(model.coef_):
        print(f'{X.columns[i]}: {coef}')

    # Intercept term (bias) in the model
    print('Wyraz wolny (bias):', model.intercept_)

    # Visualisation of the comparison of actual and predicted values and adding labels to charts
    plt.scatter(y_test, y_pred)
    # straight line for perfect match
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], '--', color='red')
    plt.xlabel('Rzeczywista liczba wypożyczonych rowerów')
    plt.ylabel('Przewidywana liczba wypożyczonych rowerów')
    plt.title('Porównanie rzeczywistych i przewidywanych wartości')
    plt.show()

    # Using polynomial regression to compare the results and find which method is better for this data

    # Creating polynomial features of degree 2
    poly = PolynomialFeatures(degree=2)
    X_poly = poly.fit_transform(X_train)

    # Fitting a linear regression model to polynomial features
    model_poly = LinearRegression()
    model_poly.fit(X_poly, y_train)

    # Prediction made on testing data
    X_test_poly = poly.transform(X_test)
    y_pred_poly = model_poly.predict(X_test_poly)

    # Regression coefficients
    print('Współczynniki regresji (po zastosowaniu regresji wielomianowej):')
    print('Wyraz wolny (bias):', model_poly.intercept_)
    for i, coef in enumerate(model_poly.coef_):
        print(f'Współczynnik dla cechy {i}: {coef}')

    # Visualization of the comparison of actual and predicted values
    plt.scatter(y_test, y_pred_poly)
    # straight line for perfect match
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], '--', color='red')
    plt.xlabel('Rzeczywista liczba wypożyczonych rowerów')
    plt.ylabel('Przewidywana liczba wypożyczonych rowerów (regresja wielomianowa)')
    plt.title('Porównanie rzeczywistych i przewidywanych wartości (regresja wielomianowa)')
    plt.show()

    # Creating polynomial features of degree 3
    poly = PolynomialFeatures(degree=3)
    X_poly = poly.fit_transform(X_train)

    # Fitting a linear regression model to polynomial features
    model_poly = LinearRegression()
    model_poly.fit(X_poly, y_train)

    # Prediction made on testing data
    X_test_poly = poly.transform(X_test)
    y_pred_poly = model_poly.predict(X_test_poly)

    # Regression coefficients
    print('Współczynniki regresji (po zastosowaniu regresji wielomianowej stopnia 3):')
    print('Wyraz wolny (bias):', model_poly.intercept_)
    for i, coef in enumerate(model_poly.coef_):
        print(f'Współczynnik dla cechy {i}: {coef}')

    # Visualization of the comparison of actual and predicted values
    plt.scatter(y_test, y_pred_poly)
    # straight line for perfect match
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], '--', color='red')
    plt.xlabel('Rzeczywista liczba wypożyczonych rowerów')
    plt.ylabel('Przewidywana liczba wypożyczonych rowerów (regresja wielomianowa stopnia 3)')
    plt.title('Porównanie rzeczywistych i przewidywanych wartości (regresja wielomianowa stopnia 3)')
    plt.show()

    # Creating polynomial features of degree 4
    poly = PolynomialFeatures(degree=4)
    X_poly = poly.fit_transform(X_train)

    # Fitting a linear regression model to polynomial features
    model_poly = LinearRegression()
    model_poly.fit(X_poly, y_train)

    # Prediction made on testing data
    X_test_poly = poly.transform(X_test)
    y_pred_poly = model_poly.predict(X_test_poly)

    # Regression coefficient
    print('Współczynniki regresji (po zastosowaniu regresji wielomianowej stopnia 4):')
    print('Wyraz wolny (bias):', model_poly.intercept_)
    for i, coef in enumerate(model_poly.coef_):
        print(f'Współczynnik dla cechy {i}: {coef}')

    # Visualisation of comparison of real and testing data
    plt.scatter(y_test, y_pred_poly)
    # straight line for perfect match
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], '--', color='red')
    plt.xlabel('Rzeczywista liczba wypożyczonych rowerów')
    plt.ylabel('Przewidywana liczba wypożyczonych rowerów (regresja wielomianowa stopnia 4)')
    plt.title('Porównanie rzeczywistych i przewidywanych wartości (regresja wielomianowa stopnia 4)')
    plt.show()
