import math


def correlation_p(array1: list, array2: list) -> float:
    """скрипт для расчета корреляции Пирсона между
    двумя случайными величинами (двумя массивами)"""

    if len(array_1) != len(array_2):
        raise ValueError("Массивы должны быть одинаковой длины")

    n = len(array_1)

    mean_1 = sum(array_1) / n
    mean_2 = sum(array_2) / n


    var_1 = sum([(xi - mean_1) ** 2 for xi in array_1]) / float(len(array_1))
    var_2 = sum([(yi - mean_2) ** 2 for yi in array_2]) / float(len(array_2))

    covariance = sum([(xi - mean_1) * (yi - mean_2) for xi, yi in zip(array_1, array_2)]) / float(n)
    correlation = round(covariance / (math.sqrt(var_1 * var_2)), 2)

    return correlation


if __name__ == '__main__':
    array_1 = [8, 3, 8, 1]
    array_2 = [1, 6, 4, 5]

    print(f"Корреляция Пирсона: {correlation_p(array_1, array_2)}")
