from typing import List, Tuple


def get_confusion_matrix(
    y_true: List[int], y_pred: List[int], num_classes: int,
) -> List[List[int]]:
    """
    Generate a confusion matrix in a form of a list of lists. 

    :param y_true: a list of ground truth values
    :param y_pred: a list of prediction values
    :param num_classes: number of supported classes

    :return: confusion matrix
    """
    ...
    # Długości y_true i y_pred mają być jednakowe
    if len(y_true) != len(y_pred):
        raise ValueError("Invalid input shapes! Długości y_true i y_pred mają być jednakowe.")

    # Ilość klas ma byc dodatnia
    if num_classes <= 0:
        raise ValueError("Invalid input! Ilość klas ma byc dodatnia.")

    # Predicted classes mają być w zakresie [0, num_classes)
    if any(pred < 0 or pred >= num_classes for pred in y_pred):
        raise ValueError("Invalid prediction classes! Predicted classes mają być w zakresie [0, num_classes).")

    # Wprowadzamy do confusion matrix zera
    confusion_matrix = [[0] * num_classes for _ in range(num_classes)]

    # Iterujemy po parach y_true/y_pred i uzupełniemy confusion matrix
    for true, pred in zip(y_true, y_pred):
        confusion_matrix[true][pred] += 1

    return confusion_matrix


def get_quality_factors(
    y_true: List[int],
    y_pred: List[int],
) -> Tuple[int, int, int, int]:
    """
    Calculate True Negative, False Positive, False Negative and True Positive 
    metrics basing on the ground truth and predicted lists.

    :param y_true: a list of ground truth values
    :param y_pred: a list of prediction values

    :return: a tuple of TN, FP, FN, TP
    """
    ...
    # Inicjalizujemy zerami liczniki dla True Negative (TN), False Positive (FP), False Negative (FN), True Positive (TP)
    TN = FP = FN = TP = 0

    # Iterujemy po parach y_true/y_pred i uzupełniemy confusion matrix ilościami
    for true, pred in zip(y_true, y_pred):
        if true == 0 and pred == 0:
            TN += 1
        elif true == 0 and pred == 1:
            FP += 1
        elif true == 1 and pred == 0:
            FN += 1
        elif true == 1 and pred == 1:
            TP += 1

    return TN, FP, FN, TP


def accuracy_score(y_true: List[int], y_pred: List[int]) -> float:
    """
    Calculate the accuracy for given lists.
    :param y_true: a list of ground truth values
    :param y_pred: a list of prediction values

    :return: accuracy score
    """
    ...
    # Inicjalizujemy ilość dla correct predictions
    correct = 0

    # Iterujemy po parach y_true/y_pred i zliczamy correct predictions
    for true, pred in zip(y_true, y_pred):
        if true == pred:
            correct += 1

    # Obliczamy accuracy jak stosunek predictions do ogólnego predictions
    accuracy = correct / len(y_true)

    return accuracy


def precision_score(y_true: List[int], y_pred: List[int]) -> float:
    """
    Calculate the precision for given lists.
    :param y_true: a list of ground truth values
    :param y_pred: a list of prediction values

    :return: precision score
    """
    ...
    # Inicjalizujemy zerami liczniki dla False Positive (FP) i True Positive (TP)
    FP = TP = 0

    # Iterujemy po parach y_true/y_pred i zliczamy TP i FP
    for true, pred in zip(y_true, y_pred):
        if true == 1 and pred == 1:
            TP += 1
        elif true == 0 and pred == 1:
            FP += 1

    # Obliczamy precizje jak stosunek TP do (TP + FP), oprócz dzielenia na zero
    if TP + FP == 0:
        precision = 0.0
    else:
        precision = TP / (TP + FP)

    return precision


def recall_score(y_true: List[int], y_pred: List[int]) -> float:
    """
    Calculate the recall for given lists.
    :param y_true: a list of ground truth values
    :param y_pred: a list of prediction values

    :return: recall score
    """
    ...
    # Inicjalizujemy zerami liczniki dla true positive (TP) i false negative (FN)
    TP = FN = 0

    # Iterujemy po parach y_true/y_pred i zliczamy TP i FN
    for true, pred in zip(y_true, y_pred):
        if true == 1 and pred == 1:
            TP += 1
        elif true == 1 and pred == 0:
            FN += 1

    # Obliczamy recall jak stosunek TP do (TP + FN), oprócz dzielenia na zero
    if TP + FN == 0:
        recall = 0.0
    else:
        recall = TP / (TP + FN)

    return recall


def f1_score(y_true: List[int], y_pred: List[int]) -> float:
    """
    Calculate the F1-score for given lists.
    :param y_true: a list of ground truth values
    :param y_pred: a list of prediction values

    :return: F1-score
    """
    ...
    # Obliczamy precision i recall przy wykorzystaniu odpowiednich funkcji
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)

    # Obliczamy F1-score jak  średnia harmoniczna precision i recall, oprócz dzielenia na zero
    if precision + recall == 0:
        f1 = 0.0
    else:
        f1 = 2 * (precision * recall) / (precision + recall)

    return f1
