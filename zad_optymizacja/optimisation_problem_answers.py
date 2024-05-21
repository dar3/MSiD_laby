from typing import Callable, List, Tuple

import numpy as np
from scipy import optimize

def income(x_1: float, x_2: float) -> float:
    """Income from production of chicken."""
    return 13 * x_1 + 25 * x_2

def objective(decision_vars: Tuple[float, float]) -> float:
    """Objective function (i.e. adapted income to optimisation jargon)."""
    x_1, x_2 = decision_vars
    return -income(x_1, x_2)

def constr_flesh(decision_vars: Tuple[float, float]) -> float:
    """Constraint according to substrate: flesh."""
    x_1, x_2 = decision_vars
    return 1000 - (0.5 * x_1 + 0.9 * x_2)

def constr_filler(decision_vars: Tuple[float, float]) -> float:
    """Constraint according to substrate: filler."""
    x_1, x_2 = decision_vars
    return 500 - (1/3 * x_1)

def constr_salt(decision_vars: Tuple[float, float]) -> float:
    """Constraint according to substrate: salt."""
    x_1, x_2 = decision_vars
    return 250 - (1/6 * x_1 + 0.1 * x_2)

def constr_x_1(decision_vars: Tuple[float, float]) -> float:
    """Constraint according to x_1 decision variable."""
    x_1, _ = decision_vars
    return x_1

def constr_x_2(decision_vars: Tuple[float, float]) -> float:
    """Constraint according to x_2 decision variable."""
    _, x_2 = decision_vars
    return x_2

def optimise() -> Tuple[float, float]:
    """Main optimisation method."""
    x0 = [0, 0]
    constraints = [constr_flesh, constr_filler, constr_salt, constr_x_1, constr_x_2]
    x_opt = optimize.fmin_cobyla(
        func=objective,
        x0=x0,
        cons=constraints,
    )
    print(x_opt)
    return x_opt

# ########## Entrypoint to the task ##############
# Run this sctipt as an entrypoint to see results
##################################################

if __name__ == "__main__":

    x_1_opt, x_2_opt = optimise()

    print(f"Found optimal solution:")
    print(f"\tas: x_1: {round(x_1_opt, 2)} [kg], x_2: {round(x_2_opt, 2)} [kg]")
    print(f"\tmaximised income: {round(income(x_1_opt, x_2_opt))} [zł]")

    print(f"Constraint flesh: {round(constr_flesh([x_1_opt, x_2_opt]), 2)}")
    print(f"Constraint filler: {round(constr_filler([x_1_opt, x_2_opt]), 2)}")
    print(f"Constraint salt: {round(constr_salt([x_1_opt, x_2_opt]), 2)}")
