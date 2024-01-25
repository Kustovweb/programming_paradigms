from functools import reduce
from math import sqrt
def correlation(data_x:list, data_y:list) -> float:
    if len(data_x) != len(data_y):
        raise IndexError("Неправильные последовательности")
    n = len(data_x)
    x_avg = sum(data_x) / n
    y_avg = sum(data_y) / n
    xy_avg = reduce(lambda x, y: x + y[0] * y[1], zip(data_x, data_y), 0) / n
    x_avg_square = (sum(list(map(lambda x: x ** 2, data_x)))) / n
    y_avg_square = (sum(list(map(lambda y: y ** 2, data_y)))) / n
    dispersion_x = x_avg_square - (x_avg ** 2)
    dispersion_y = y_avg_square - (y_avg ** 2)
    r_empire = (xy_avg - x_avg * y_avg) / (sqrt(dispersion_x) * sqrt(dispersion_y))
    return r_empire

print(correlation([1, 2, 3, 4, 5, 6, 7, 8], [3, 3, 4, 5, 5, 6, 8, 10]))

