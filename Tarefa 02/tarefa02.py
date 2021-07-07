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


def anguloOrientado(x, degrees=True):
    mult = 1
    if x[1] < 0:
        mult = -1
    if not degrees:
        return mult*math.acos(x[0]/norma(x))
    return mult*math.acos(x[0]/norma(x))*(180/math.pi)


def pseudoAngulo(x, y, degrees=True):
    if not degrees:
        return 1-(prodescalar(x, y)/(norma(x)*norma(y)))
    return (1-(prodescalar(x, y)/(norma(x)*norma(y))))*(180/math.pi)


def pseudoAnguloOrientado(x, degrees=True):
    if x[0] >= 0:
        if x[1] >= 0:
            if x[0] >= x[1]:
                return x[1]/x[0]
            return 2-(x[0]/x[1])
        if -x[0] <= x[1]:
            return 2+(-x[0]/x[1])
        return 4-(x[1]/-x[0])
    if x[0] < 0:
        if -x[0] >= -x[1]:
            return 4+(-x[1]/-x[0])
        return 6-(-x[0]/-x[1])
    if x[0] <= -x[1]:
        return 6+(x[0]/-x[1])
    return 8-(-x[1]/x[0])


def prodvetorial(x, y):
    if len(x) == 2:
        return x[0]*y[1]-x[1]*y[0]
    return [x[1]*y[2]-x[2]*y[2], x[2]*y[0]-x[0]*y[2], x[0]*y[1]-x[1]*y[0]]


print(somavetorial([0, 2, 3], [1, 2, 0]))
print(multescalar(2, [1, 1]))
print(prodescalar([1, 2, 3], [3, 2, 1]))
print(norma([1, 2]))
print(distancia([3, 3], [0, 0]))
print(angulo([2, -4, -1], [0, 5, 2]))
print(anguloOrientado([0, 1]))
print(anguloOrientado([0, -1]))
print(pseudoAngulo([2, -4, -1], [0, 5, 2]))
print(pseudoAngulo([1, 0], [0, 1], False))
print(pseudoAnguloOrientado([10,5]))
print(prodvetorial([1, 0, 0], [0, 1, 0]))
print(prodvetorial([1, 0], [0, 1]))

print()
print(prodescalar([1,0], [0,1]))
print(pseudoAngulo([1,0], [0,1], False))
print(anguloOrientado([1,0], True))