import math


def somavetorial(x, y):
    z = []
    for i in range(len(x)):
        z.append(x[i]+y[i])
    return z


def multescalar(lamb: int, x: list) -> list:
    z = []
    for i in range(len(x)):
        z.append(lamb*x[i])
    return z


def prodescalar(x, y):
    z = []
    for i in range(len(x)):
        z.append(x[i]*y[i])
    return sum(z)


def norma(x):
    z = 0
    for i in range(len(x)):
        z += x[i]**2
    return math.sqrt(z)


def distancia(x, y):
    """Returns the distance between vectors x and y.

    Args:
        x (list): list containing points from vector x.
        y (list): list containing points from vector y.

    Returns:
        [float]: [the distance between vectors x and y]
    """
    z = []
    for i in range(len(x)):
        z.append(x[i]-y[i])
    return norma(z)


def angulo(x, y, degrees=True):
    """Returns the angle between vectors x and y.

    Args:
        x (list): list containing points from vector x.
        y (list): list containing points from vector y.
        degrees (bool): if the result should be in degrees or radians, defaults to True.
    Returns:
        float: the angle between the two vectors
    """

    if not degrees:
        return math.acos(prodescalar(x, y)/(norma(x)*norma(y)))
    return math.acos(prodescalar(x, y)/(norma(x)*norma(y)))*(180/math.pi)


print(somavetorial([0, 2, 3], [1, 2, 0]))
print(multescalar(2, [1, 1]))
print(prodescalar([1, 2, 3], [3, 2, 1]))
print(norma([1, 2]))
print(distancia([3, 3], [0, 0]))
print(angulo([2, -4, -1], [0, 5, 2]))
