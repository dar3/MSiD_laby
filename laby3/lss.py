"""
Task: implement LSS method.

Here are some useful hints:
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.lstsq.html
# https://www.statsoft.pl/textbook/stathome_stat.html?https%3A%2F%2Fwww.statsoft.pl%2Ftextbook%2Fstglm.html
"""
import urllib.request
import os
from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def fetch_data_file() -> str:
    """Download a file with target data to fit LSS algo in."""
    file = "GDP_happiness.csv"
    url_server = "https://byes.pl/wp-content/uploads/datasets/" + file
    if not os.path.isfile(file):
        urllib.request.urlretrieve(url_server, file)
    else:
        print(f"File already exists!")
    return file


def read_data_vectors() -> Tuple[np.ndarray, np.ndarray]:
    """Read target data and obtain X and Y vectors without NaNs."""
    gdp_happines_df = pd.read_csv(fetch_data_file(), index_col=[0])
    gdp_happines_df = gdp_happines_df.fillna(gdp_happines_df.mean(axis=0))
    gdp_happines_df.tail()

    X = gdp_happines_df["GDP per capita"].values
    Y = gdp_happines_df["happiness"].values

    return X, Y


def get_polynomial_form(polynomial_degree: int) -> np.ndarray:
    """
    Get array with form of polynomial.

    :param polynomial_degree: a degree of polynomial
        [[0], [1]] - 1st order, [[0], [1], [2]] - 2nd order, 
        [[0], [1], [2], [3]] - 3rd order, and so on...
    :return: a array with degrees of polynomial
    """
    ...
    result = []
    for i in range(polynomial_degree + 1):
        result.append([i])
    return np.array(result)


def print_polynomial(theta: np.ndarray, precission: int = 3) -> str:
    """Return string representation of polynomial."""
    ...

    result = ""
    for i in range(len(theta)):
        print("precision: ", precission)
        print("liczba: ", theta[i][0])
        formatted_number = format(theta[i][0], f".{precission}f").rstrip("0")
        print(formatted_number)
        if formatted_number[-1] == ".":
            formatted_number += "0"
        print(formatted_number)

        result += f"{formatted_number}*x^{i}"
        if i < len(theta) - 1:
            result += " + "
    return result
    print("TEST: ", polynomial_str)
    return polynomial_str


def least_squares_solution(
        X: np.ndarray, Y: np.ndarray, polynomial_degree: int
) -> np.ndarray:
    """
    Compute theta matrix with coefficients of polynomial fitted by LSS.

    :param X: argument vector, shape = (N, )
    :param Y: target vector, shape = (N, ) 
    :param polynomial_degree: degree of fitted polynomial

    :return: theta matrix of polynomial, shape = (1, polynomial_degree + 1)
    """
    ...
    # exponents - struktura przechowujaca stopnie wielomianu
    # power - zmienna używana iteracyjnie do generowania kolejnych potęg argumentu X
    exponents = np.arange(polynomial_degree + 1)
    # Macierz projektowania M, która będzie zawierać potęgi argumentu X dla każdego stopnia wielomianu.
    M = np.array([X**power for power in exponents]).T
    # używamy funkcji np.linalg.lstsq do oblicznia wsp wielomianu. Wybieramy pierwszy element krotki [0]
    T = np.linalg.lstsq(M, Y, rcond=None)[0]
    # zmierniami tablice jednowymiarową na jednokolumnową z dowolną ilością wierszy.
    # zwracamy tablicę wynikową, która zawiera współczynniki wielomianu
    return T.reshape(-1, 1)


def generalised_linear_model(X: np.ndarray, T: np.ndarray) -> np.ndarray:
    """
    Compute values for generalised linear model.

    :param X: argument vector, shape = (N, )
    :param T: theta matrix of polynomial, shape = (1, polynomial_degree + 1)
    :return: regressed values, shape = (N, )
    """
    return sum([coeff * X ** degree for degree, coeff in enumerate(T)])
    # sekwencję liczb od 0 do polynomial_degree. Ta sekwencja liczb odpowiada stopniom wielomianu.
    # generujemy tablicę zawierająca potęgi elementów wektora X dla każdego stopnia wielomianu.
    # Sumujemy te wartości dla każdej próbki z parametrem axis=1, co oznacza sumowanie po wierszach.
    # return np.sum(T * (X ** np.arange(T.shape[1])), axis=1)


def visualise_LSS_method(X: np.ndarray, Y: np.ndarray, T: np.ndarray):
    """
    Visualise LSS model on fancy Matplotlib plot.

    :param X: input argument vector
    :param Y: input target vector
    :param T: theta vector with coefficients of ploynomial
    """
    X_test = np.linspace(start=X.min(), stop=X.max(), num=300)
    Y_pred = generalised_linear_model(X_test, T)
    plt.scatter(X, Y, color="tab:blue", label="real data")
    plt.plot(X_test, Y_pred, color="tab:orange", label="estimated function")
    plt.xlabel("x - GDP", fontsize=14)
    plt.ylabel("y - happiness", fontsize=14)
    plt.title(f"Fitted: \n {print_polynomial(T, precission=5)}")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # here is a playground for your tests!
    X, Y = read_data_vectors()
    T = least_squares_solution(X, Y, 2)
    print(print_polynomial(T))
    visualise_LSS_method(X, Y, T)


#     Metoda najmniejszych kwadratów to sposób znajdowania najlepszego dopasowania linii lub krzywej do zestawu punktów danych. Polega na znalezieniu takiej linii lub krzywej, która minimalizuje sumę kwadratów odległości między punktami
#     danych a odpowiadającymi im punktami na linii lub krzywej.
