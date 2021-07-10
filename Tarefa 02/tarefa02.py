import math


def somavetorial(x, y):
    z = []
    for i in range(len(x)):
        z.append(x[i]+y[i])
    return z


def subtrvetorial(x, y):
    z = []
    for i in range(len(x)):
        z.append(x[i]-y[i])
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


def angulo(x, y, degrees=False):
    """Returns the angle between vectors x and y.

    Args:
        x (list): list containing points from vector x.
        y (list): list containing points from vector y.
        degrees (bool): if the result should be in degrees or radians, defaults to False.
    Returns:
        float: the angle between the two vectors
    """

    if not degrees:
        return math.acos(prodescalar(x, y)/(norma(x)*norma(y)))
    return math.acos(prodescalar(x, y)/(norma(x)*norma(y)))*(180/math.pi)


def anguloOrientado(x, degrees=False):
    mult = 1
    if x[1] < 0:
        mult = -1
    if not degrees:
        return mult*math.acos(x[0]/norma(x))
    return mult*math.acos(x[0]/norma(x))*(180/math.pi)


def pseudoAnguloCosseno(x, y, degrees=False):
    if not degrees:
        return 1-(prodescalar(x, y)/(norma(x)*norma(y)))
    return (1-(prodescalar(x, y)/(norma(x)*norma(y))))*(180/math.pi)


def pseudoAnguloOrientado(x):
    if x[1] >= 0:
        if x[0] >= 0:
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


def pseudoAngulo2(x, y):
    print("PSEUDOS", pseudoAnguloOrientado(x), pseudoAnguloOrientado(y))
    return pseudoAnguloOrientado(x)-pseudoAnguloOrientado(y)


def prodvetorial(x, y):
    if len(x) == 2:
        return x[0]*y[1]-x[1]*y[0]
    return [x[1]*y[2]-x[2]*y[2], x[2]*y[0]-x[0]*y[2], x[0]*y[1]-x[1]*y[0]]


def intersect(a, b, c, d):
    ab = subtrvetorial(b, a)
    ac = subtrvetorial(c, a)
    ad = subtrvetorial(d, a)
    ca = subtrvetorial(a, c)
    cb = subtrvetorial(b, c)
    cd = subtrvetorial(d, c)

    r1 = prodvetorial(ab, ac)*prodvetorial(ab, ad) < 0
    r2 = prodvetorial(cd, ca)*prodvetorial(cd, cb) < 0
    return r1 and r2


def area(x, y):
    if len(x) == 2:
        return abs(prodvetorial(x, y))
    return norma(prodvetorial(x, y))


def antiHorario(listaDePontos):
    res = 0
    for i in range(len(listaDePontos)-1):
        res += prodvetorial(listaDePontos[i], listaDePontos[i+1])
    res += prodvetorial(listaDePontos[0], listaDePontos[-1])
    return 0.5*res > 0


# print(somavetorial([0, 2, 3], [1, 2, 0]))
# print(multescalar(2, [1, 1]))
# print(prodescalar([1, 2, 3], [3, 2, 1]))
# print(norma([1, 2]))
# print(distancia([3, 3], [0, 0]))
# print(angulo([2, -4, -1], [0, 5, 2]))
# print(anguloOrientado([0, 1]))
# print(anguloOrientado([0, -1]))
# print(pseudoAnguloCosseno([2, -4, -1], [0, 5, 2]))
# print(pseudoAnguloCosseno([1, 0], [0, 1], False))
# print(pseudoAnguloOrientado([10,5]))
# print(prodvetorial([1, 0, 0], [0, 1, 0]))
# print(prodvetorial([1, 0], [0, 1]))

# print(prodescalar([1,2], [2,1]))
# print(pseudoAngulo2([1, 0], [0, 1]))

# print("Se positivo a está a esquerda de b:", pseudoAngulo2([1, 1], [1, -1]))
# print("Se positivo a está a esquerda de b:", pseudoAngulo2([1, -1], [1, 1]))

# print("Interseção dos segimentos de retas: ",intersect((0, 0), (2, 2), (0, 1), (2, 1)))
# print("Interseção dos segimentos de retas: ",intersect((0, 0), (2, 2), (0, 1), (2, 1)))
# print("Interseção dos segimentos de retas: ",intersect((0, 0), (2, 2), (0, 6), (9, -3)))
# print("Interseção dos segimentos de retas: ",intersect((0, -2), (6, 4), (0, 6), (9, -3)))

print(antiHorario([(0, 0), (0, 1), (2, 0)]))
print(antiHorario([(0, 0), (2, 0), (0, 1)]))
print(area((0,1), (2,0)))
print(area((0,1,3), (2,0,4)))
